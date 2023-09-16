
import numpy as np

# Create the larger array
larger_array = np.array([[0] * 10] * 24)

# Create the smaller array
smaller_array = np.array([[0, 1, 1, 0], [0, 1, 1, 0]])

# Define the position to insert the smaller array
position = (2, 2)

# Get the shape of the smaller array
smaller_shape = smaller_array.shape

# Get the indices to insert the smaller array
indices = tuple(slice(position[i], position[i] + smaller_shape[i]) for i in range(len(smaller_shape)))

# Add the smaller array to the larger array
larger_array[indices] += smaller_array

# Print the updated larger array
print(larger_array)