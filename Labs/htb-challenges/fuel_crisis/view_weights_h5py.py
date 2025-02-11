import h5py

# Load the file
f = h5py.File('ai_ml_fuel_crisis/challenge/application/models/model.h5', 'r')

# The file object is the starting point
# h5py.File acts like a python dictionary so we can check the keys with 
print(f'The keys or groups for the file are:\n {list(f.keys())}\n')

# The root group is the file so we will print the name of the root group as proof-of-concept
print(f'The root group name is {f.name}')

# There are 2 datasets so we will set 2 variables for them and get the shape and data types for each 
# Establishing data set 1
dset1 = f['model_weights']
# Print the name of the dataset
print(f'The name of dataset 1 is {dset1.name}')

# Establishing data set 2
dset2 = f['optimizer_weights']
# Print the name of the dataset
print(f'The name of dataset 2 is {dset2.name}')
