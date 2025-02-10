import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import cv2
from sklearn.manifold import TSNE
import plotly.graph_objects as go

# Load the data
data = np.load('token_embeddings.npz')

# Print the data information
print(f'Printed data: {data}')

# Print the keys in the file
print(f'Printed keys: {data.keys()}')

# Generate a list of the keys
keys = list(data.keys())

# Print out any metadata
# There is no metadata
# print(f'Printed metadata: {data["metadata"]}')

# Print the data files
# print(f'Printed data files: {data.files}')

# Print the shape of the data
# Has no shape
# print(f'Printed data shape: {data.shape}')

# Print the tokens
# print(f'Printed tokens: {data["tokens"]}')

# Print the data type of the tokens
# print(f'Printed tokens data type: {data["tokens"].dtype}')

# Print the token shape
# print(f'Printed token shape: {data["tokens"].shape}')

# Print the embeddings
# print(f'Printed embeddings: {data["embeddings"]}')

# Print the data type of the embeddings
# print(f'Printed embeddings data type: {data["embeddings"].dtype}')

# Print the embeddings shape
# print(f'Printed embeddings shape: {data["embeddings"].shape}')

# Check the shape of the stored arrays
shapes = {key: data[key].shape for key in keys}

# Extract the 'embeddings' array from the loaded data
# Shape is 512-dimensional vectors
embeddings = data['embeddings']

# Extract the 'tokens' array from the loaded data
# Shape is 110
tokens = data['tokens']

# Create a tesseract-like structure (a 4D tensor)
# Here you might want to combine the tokens and embeddings in some form
# tesseract = np.expand_dims(embeddings, axis=-1) # Adding a dimension to make it 3D
# tesseract = np.repeat(tesseract, 10, axis=-1) # Repeat to create a 4D structure

# print(f'Tesseract shape: {tesseract.shape}')

# get the overall min and max values
min_value = np.min(embeddings)
max_value = np.max(embeddings)

# Print the min and max values
print(f'Minimum value: {min_value}')
print(f'Maximum value: {max_value}')

# Reduce the dimensions to 4D using Principal Component Analysis (PCA)
# Helps to retain the most important variance in the data while reducing dimensions
# pca = PCA(n_components=4) # Specify 4D as the target dimension
# embeddings_4d = pca.fit_transform(embeddings) # Perform dimensionality reduction

# Project the 4D embeddings to 3D for visualization
# Since we cannot directly visualize 4D data, we drop the last dimension (4th) to obtain 3D data
# This is a simple projection method where we can ignore one of the dimensions
# fig = plt.figure(figsize=(10, 7)) # Create a figure for the plot
# ax = fig.add_subplot(111, projection='3d') # Create a 3D scatter plot

# Scatter plot using the first 3 principal components
# ax.scatter(embeddings_4d[:, 0], embeddings_4d[:, 1], embeddings_4d[:, 2], 
#           c='green', marker='o') # Green dots for visulaization

# Label the graph for better understanding 
# ax.set_title("Projected 4D embeddings into 3D") # Title of the plot
# ax.set_xlabel("Component 1") # Label for the x-axis
# ax.set_ylabel("Component 2") # Label for the y-axis
# ax.set_zlabel("Component 3") # Label for the z-axis

# Display the plot
# plt.show()

# DIDNT WORK
# Creating image object of the array
# cv2.imwrite('output_image.png', embeddings_4d)

# DIDNT WORK
# Reduce to 4D first
# tsne = TSNE(n_components=4, perplexity=30, random_state=42)
# embeddings_4d_tsne = tsne.fit_transform(embeddings)

# Take the first 3 dimensions for visualization
# tsne_fig = plt.figure(figsize=(8, 6))
# tsne_ax = tsne_fig.add_subplot(111, projection='3d')
# tsne_ax.scatter(embeddings_4d_tsne[:, 0], embeddings_4d_tsne[:, 1], embeddings_4d_tsne[:, 2], alpha=.06)

# tsne_ax.set_xlabel('Dim 1')
# tsne_ax.set_ylabel('Dim 2')
# tsne_ax.set_zlabel('Dim 3')
# tsne_ax.set_title('4D to 3D Projection of Embeddings')
# plt.show()

# trying to show 3d image with shadows using plotly
# Reduce to 3D using PCA
# pca = PCA(n_components=3)
# embeddings_3d = pca.fit_transform(embeddings)

# # Create a 3D scatter plot
# fig = go.Figure(
#     data=[go.Scatter3d(
#         x=embeddings_3d[:, 0],
#         y=embeddings_3d[:, 1],
#         z=embeddings_3d[:, 2],
#         mode='markers',
#         marker=dict(
#             size=5,
#             color=embeddings_3d[:, 2], # Color by Z value
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )]
# )

# # Add shadow effect with lighting
# fig.update_layout(
#     scene=dict(
#         xaxis_title='PCA 1',
#         yaxis_title='PCA 2',
#         zaxis_title='PCA 3',
#         aspectmode='cube',
#         camera=dict(
#             eye=dict(x=1.5, y=1.5, z=0.5) # Adjust camera angle for better depth
#         )
#     ),
#     template='plotly_dark' # Dark theme for better contrast
# )

# fig.show()

# Transforming embeddings into a two-dimensional space
# Fit method computes the components from the data by determining the axes. it learns the structure of the data
# Transform method reduces the dimensionality by providing new coordinates
pca = PCA(n_components=2)
re_embeddings = pca.fit_transform(embeddings)

# Create a scatter plot of the embeddings
plt.figure(figsize=(20, 12))
plt.scatter(re_embeddings[:, 0], re_embeddings[:, 1], alpha=0.6, s=100, edgecolor='k')
for i, token in enumerate(tokens):
    plt.text(re_embeddings[i, 0] + 0.02, re_embeddings[i, 1], str(token), fontsize=12, fontweight='bold')
    
plt.title('Token Embeddings PCA:')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2') 
plt.grid(False)
plt.show()