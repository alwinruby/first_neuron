import numpy as np

# Values from the previous output when we described
# what a neural network is
layer_outputs = [4.8, 1.21, 2.385]
# e - mathematical constant, we use E here to match a common coding
# style where constants are uppercased
E = 2.71828182846 # you can also use math.e
# For each value in a vector, calculate the exponential value
exp_values = []
for output in layer_outputs:
    exp_values.append(E ** output) # ** - power operator in Python

print('exponentiated values:')
print(exp_values)