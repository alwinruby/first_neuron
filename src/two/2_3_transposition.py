import numpy as np

a = [1, 2, 3]
b = [2, 3, 4]

a = np.array([a])
b = np.array([b]).T

print(np.dot(a, b))


# achieved the same result as the dot product of two vectors, but performed on matrices
# and returning a matrix

# NumPy does not have a dedicated method for performing matrix product — the dot product and
# matrix product are both implemented in a single method: np.dot().
