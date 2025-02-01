import time
import cupy as cp
from pykalman import KalmanFilter

# Load the .npy file into a CuPy array
data = cp.load('distance_matrix.npy')

# Start the timer
start_time = time.time()

# Define the initial state for the Kalman filter
initial_state = data[0, :]
initial_covariance = cp.eye(data.shape[1])

# Transition and observation matrices
transition_matrix = cp.eye(data.shape[1])
observation_matrix = cp.eye(data.shape[1])

# Convert matrices to NumPy for compatibility with pykalman
transition_matrix_np = cp.asnumpy(transition_matrix)
observation_matrix_np = cp.asnumpy(observation_matrix)
initial_state_np = cp.asnumpy(initial_state)
initial_covariance_np = cp.asnumpy(initial_covariance)

# Initialize Kalman Filter
kf = KalmanFilter(
    transition_matrices=transition_matrix_np,
    observation_matrices=observation_matrix_np,
    initial_state_mean=initial_state_np,
    initial_state_covariance=initial_covariance_np
)

# Kalman filter update loop (without Numba)
state_means = []
state_covariances = []
for i in range(data.shape[0]):
    if i == 0:
        state_mean, state_covariance = kf.filter_update(initial_state_np, initial_covariance_np, cp.asnumpy(data[i]))
    else:
        state_mean, state_covariance = kf.filter_update(state_means[-1], state_covariances[-1], cp.asnumpy(data[i]))

    state_means.append(state_mean)
    state_covariances.append(state_covariance)

    # Debugging print statement every 100 iterations
    if i % 100 == 0 and i != 0:
        elapsed_time = time.time() - start_time
        time_per_iteration = elapsed_time / i
        estimated_total_time = time_per_iteration * data.shape[0]
        remaining_time = estimated_total_time - elapsed_time
        print(f"Iteration {i}/{data.shape[0]}, Elapsed Time: {elapsed_time:.2f}s, Estimated Remaining Time: {remaining_time:.2f}s")

# Convert lists to CuPy arrays
state_means = cp.array(state_means)
state_covariances = cp.array(state_covariances)

# End the timer
end_time = time.time()

# Print results
print("Analyzed results of the Kalman filter:")
print("Estimated State Means:\n", cp.asnumpy(state_means))
print("Estimated State Covariances:\n", cp.asnumpy(state_covariances))
print(f"Total Time Taken: {end_time - start_time:.2f} seconds")