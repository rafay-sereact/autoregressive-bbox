import numpy as np

# Extract the k array from the CameraInfo message
k_array = np.array([5.99027979e+03, 0.00000000e+00, 2.25877563e+03, 0.00000000e+00,
                   5.98936230e+03, 2.23563940e+03, 0.00000000e+00, 0.00000000e+00,
                   1.00000000e+00])

# Reshape into 3x3 matrix
K_matrix = k_array.reshape(3, 3)

print('3x3 Camera Intrinsic Matrix:')
print(K_matrix)
print()
print('Matrix shape:', K_matrix.shape)
print('Matrix dtype:', K_matrix.dtype)

# Also save as a variable for easy copying
print('\nAs numpy array:')
print('K = np.array(')
print(K_matrix.tolist())
print(')')
