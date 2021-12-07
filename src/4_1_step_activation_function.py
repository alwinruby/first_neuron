# activation function serves is to mimic a neuron “firing” or “not firing”
# based on input information. The simplest version of this is a step function. In a single neuron, if
# the weights · inputs + bias results in a value greater than 0, the neuron will fire and output a 1;
# otherwise, it will output a 0.

# A linear function is simply the equation of a line. It will appear as a straight line when graphed,
# where y=x and the output value equals the input.

# First off, what’s a nonlinear function? A nonlinear function cannot be represented well by a
# straight line, such as a sine function

# Linear Activation in the Hidden Layers

import numpy as np

# inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
#
# output = []
# for i in inputs:
#     if i > 0:
#         output.append(i)
#     else:
#         output.append(0)

# inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
# output = []
# for i in inputs:
#     output.append(max(0, i))

inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
output = np.maximum(0, inputs)

print(output)

