# Depicting how the dot product fits in to the calculation of inputs,
# weights, and biases for an entire layer of neurons in a neural network.
import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2.0, 3.0, 0.5]

outputs = np.dot(weights, inputs) + biases

print(outputs)

# np.dot(weights, inputs) = [np.dot(weights[0], inputs),
#                            np.dot(weights[1], inputs),
#                            np.dot(weights[2], inputs)] \
#     = [2.8, -1.79, 1.885]

# This syntax involving the dot product of weights and inputs followed by the vector addition of
# bias is the most commonly used way to represent this calculation of inputs·weights+bias. To
# explain the order of parameters we are passing into np.dot(), we should think of it as whatever
# comes first will decide the output shape. In our case, we are passing a list of neuron weights first
# and then the inputs, as our goal is to get a list of neuron outputs. As we mentioned, a dot product
# of a matrix and a vector results in a list of dot products. The np.dot() method treats the matrix as
# a list of vectors and performs a dot product of each of those vectors with the other vector. In this
# example, we used that property to pass a matrix, which was a list of neuron weight vectors and a
# vector of inputs and get a list of dot products — neuron outputs.






