import numpy as np

softmax_output = [0.7, 0.1, 0.2]
softmax_output = np.array(softmax_output).reshape(-1, 1)

print("the softmax output reshaped")
print(softmax_output)

print("left side output multiplied by the Kronecker delta on softmax output")
print(np.eye(softmax_output.shape[0]))

print("multiplication of both of the values from the equation")
print(softmax_output * np.eye(softmax_output.shape[0]))

print("gain some speed by replacing this by the np.diagflat method call")
print(np.diagflat(softmax_output))

print("transpose the second argument to get its row vector form")
print(np.dot(softmax_output, softmax_output.T))

print("subtraction of both arrays")
print(np.diagflat(softmax_output) - np.dot(softmax_output, softmax_output.T))