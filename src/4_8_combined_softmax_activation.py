import numpy as np

# Softmax activation
class Activation_Softmax:

    # Forward pass
    def forward(self, inputs):

        # Get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1,
        keepdims=True))
        # Normalize them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1,
        keepdims=True)
        self.output = probabilities

print(np.exp(1))

print(np.exp(10))

print(np.exp(100))

#print(np.exp(1000))

print(np.exp(-np.inf), np.exp(0))

softmax = Activation_Softmax()
# softmax.forward([[1, 2, 3]])
# print(softmax.output)

softmax.forward([[-2, -1, 0]]) # subtracted 3 - max from the list
print(softmax.output)