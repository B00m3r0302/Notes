# Import the KalmanFilter class from the pykalman library
from pykalman import KalmanFilter
import time  # Import the time module to measure elapsed time
import numpy as np  # Import the NumPy library for array handling

# Load the .npy file
data = np.load('distance_matrix.npy')

# Start the timer
start_time = time.time()  # Record the start time to measure execution time

# Print the data
print(f"{data}\n")

# Print the shape of the data
print(f"Matrix shape: {data.shape}\n")

# Print the number of rows and columns in the data
num_rows, num_cols = data.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}\n")

# Define the initial state for the Kalman filter
# The initial state represents the starting point of the system. It's essentially an estimate of the state variables at the beginning of tracking.
# Assuming the first row represents the initial state
initial_state = data[0, :]
# Print the initial state
print(f"{initial_state}\n")

# Initial covariance
# The initial covariance matrix represents the uncertainty in the initial state estimate. It's a measure of how much we trust the initial state estimate.
initial_covariance = np.eye(data.shape[1])
# Print the initial covariance
print(f"{initial_covariance}\n")

# Transition matrix
# The transition model describes how the state of the system changes from one step to the next and is represented by the transition matrix A
# This matrix defines the relationship between the state at time k and the state at time k+1.
transition_matrix = np.eye(data.shape[1])  # Adjust this based on your model

# Observation matrix
# The observation model describes how the observed measurements relate to the internal state of the system and is represented by the observation matrix H
# This matrix defines the relationship between the state of the system and the measurements observed at each time step.
observation_matrix = np.eye(data.shape[1])  # Adjust this based on your model

# Initialize the Kalman filter
kf = KalmanFilter(
    transition_matrices=transition_matrix,
    observation_matrices=observation_matrix,
    initial_state_mean=initial_state,
    initial_state_covariance=initial_covariance
)

# Number of iterations (rows in the data)
n_iterations = data.shape[0]

# Apply the Kalman filter to the data with progress reporting
# Initialize lists to store the filtered state means and covariances
state_means, state_covariances = [], []

# Loop over each row in the data
for i in range(n_iterations):
    print(f"Starting iteration {i}", flush=True)
    if i == 0:
        # For the first iteration, initialize with the initial state and covariance
        filtered_state_means, filtered_state_covariances = kf.filter_update(
            initial_state, initial_covariance, data[i])
    else:
        # For subsequent iterations, update the state and covariance based on the previous state and the current observation
        filtered_state_means, filtered_state_covariances = kf.filter_update(
            filtered_state_means, filtered_state_covariances, data[i])

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

# Convert lists to numpy arrays
state_means = np.array(state_means)
state_covariances = np.array(state_covariances)

# End the timer
end_time = time.time()

# Print the analyzed results
print("Analyzed results of the Kalman filter:")
print(f"Estimated State Means:\n{state_means}\n")
print(f"Estimated State Covariances:\n{state_covariances}\n")
print(f"Total Time Taken: {end_time - start_time:.2f} seconds\n", flush=True)
