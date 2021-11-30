# the perspective of the input and weights, we need to perform the dot
# product of each input and each weight set in all of their combinations. The dot product takes the
# row from the first array and the column from the second one, but currently the data in both arrays
# are row-aligned. Transposing the second array shapes the data to be column-aligned. The matrix
# product of inputs and transposed weights will result in a matrix containing all atomic dot products
# that we need to calculate. The resulting matrix consists of outputs of all neurons after operations
# performed on each input sample

import numpy as np

inputs = [[1, 2, 3, 2.5],
          [2, 5, -1, 2],
          [-1.5, 2.7, 3.3, -0.8]]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2.0, 3.0, 0.5]

layer_outputs = np.dot(inputs, np.array(weights).T) + biases

print(np.dot(inputs, np.array(weights).T))
print()
print(biases)
print()
print(layer_outputs)