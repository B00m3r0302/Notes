# Import necessary libraries
# To handle numerical operations (e.g., loading and manipulating arrays)
import numpy as np
import matplotlib.pyplot as plt  # To create and save visualizations
# To perform multidimensional scaling (MDS) for dimensionality reduction
from sklearn.manifold import MDS

# Load the distance matrix from a .npy file
# Load a NumPy array from a saved file 'distance_matrix.npy'
data = np.load('distance_matrix.npy')

# Initialize the MDS (Multidimensional Scaling) model with 2 components
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
# n_components=2 specifies that we want to reduce the data to 2 dimensions (2D space) for visualization
# dissimilarity='precomputed' means that the input data is a distance matrix, and we are using it directly
# random_state=42 ensures reproducibility, i.e., the results will be the same each time the script runs

# Apply the MDS algorithm to the distance matrix
# The fit_transform method computes the 2D positions that represent the distances
X = mds.fit_transform(data)

# Create a scatter plot to visualize the 2D representation
# Scatter plot of the first and second columns of X, representing the 2D coordinates
plt.scatter(X[:, 0], X[:, 1])

# Save the plot as a PNG image file
# Save the plot as 'sarahMDS.png' in the current working directory
plt.savefig('sarahMDS.png')

# Display the plot to the screen
plt.show()  # Display the plot in a pop-up window or in the notebook (depending on the environment)