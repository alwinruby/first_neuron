import nnfs
from nnfs.datasets import spiral_data
import numpy as np

nnfs.init()

X, y = spiral_data(samples=100, classes=3)

class Activation_Softmax:
    def forward(self, inputs):
        # Get exponentiated normalized probabilities
        # - The subtraction is to help minimize "exploding values"
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))

        # Normalize for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)

        self.output = probabilities


softmax = Activation_Softmax()
softmax.forward([[1, 2, 3]])
print(softmax.output)