import time
import cupy as cp  # Import CuPy as cp for GPU-accelerated computations
from pykalman import KalmanFilter

# Load the .npy file into a CuPy array
data = cp.load('distance_matrix.npy')

# Start the timer
start_time = time.time()  # Record the start time to measure execution time

# Print the data (Optional: use cp.asnumpy to convert to NumPy array for printing)
print(f"{cp.asnumpy(data)}\n")

# Print the shape of the data
print(f"Matrix shape: {data.shape}\n")

# Print the number of rows and columns in the data
num_rows, num_cols = data.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}\n")

# Define the initial state for the Kalman filter
# Assuming the first row represents the initial state
initial_state = data[0, :]
print(f"{cp.asnumpy(initial_state)}\n")

# Initial covariance
initial_covariance = cp.eye(data.shape[1])
print(f"{cp.asnumpy(initial_covariance)}\n")

# Transition matrix
transition_matrix = cp.eye(data.shape[1])

# Observation matrix
observation_matrix = cp.eye(data.shape[1])

# Initialize the Kalman filter
kf = KalmanFilter(
    transition_matrices=cp.asnumpy(transition_matrix),
    observation_matrices=cp.asnumpy(observation_matrix),
    initial_state_mean=cp.asnumpy(initial_state),
    initial_state_covariance=cp.asnumpy(initial_covariance)
)

# Number of iterations (rows in the data)
n_iterations = data.shape[0]

# Apply the Kalman filter to the data with progress reporting
state_means, state_covariances = [], []

# Loop over each row in the data
for i in range(n_iterations):
    print(f"Starting iteration {i}", flush=True)
    if i == 0:
        # For the first iteration, initialize with the initial state and covariance
        filtered_state_means, filtered_state_covariances = kf.filter_update(
            cp.asnumpy(initial_state), cp.asnumpy(initial_covariance), cp.asnumpy(data[i]))
    else:
        # For subsequent iterations, update the state and covariance based on the previous state and the current observation
        filtered_state_means, filtered_state_covariances = kf.filter_update(
            cp.asnumpy(filtered_state_means), cp.asnumpy(filtered_state_covariances), cp.asnumpy(data[i]))

    state_means.append(filtered_state_means)
    state_covariances.append(filtered_state_covariances)

    # Debug print to ensure the loop is running
    if i % 10 == 0:
        print(f"Reached iteration {i}", flush=True)

    # Report progress every 100 iterations
    if i % 100 == 0 and i != 0:
        elapsed_time = time.time() - start_time
        time_per_iteration = elapsed_time / i
        estimated_total_time = time_per_iteration * n_iterations
        remaining_time = estimated_total_time - elapsed_time
        print(f"Iteration {i}/{n_iterations}, Elapsed Time: {elapsed_time:.2f} seconds, Estimated Remaining Time: {remaining_time:.2f} seconds", flush=True)

# Convert lists to numpy arrays for final output
state_means = cp.array(state_means)
state_covariances = cp.array(state_covariances)

# End the timer
end_time = time.time()

# Print the analyzed results (Optional: use cp.asnumpy to convert to NumPy array for printing)
print("Analyzed results of the Kalman filter:")
print(f"Estimated State Means:\n{cp.asnumpy(state_means)}\n")
print(f"Estimated State Covariances:\n{cp.asnumpy(state_covariances)}\n")
print(f"Total Time Taken: {end_time - start_time:.2f} seconds\n", flush=True)