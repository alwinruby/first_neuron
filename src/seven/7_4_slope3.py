import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(5))


def f(x):
    return 2 * x ** 2


y = f(x)  # Calculate function outputs for new function

print(x)
print(y)

print((y[3]-y[2]) / (x[3]-x[2]))

p2_delta = 0.0001
x1 = 1
x2 = x1 + p2_delta # add delta
y1 = f(x1) # result at the derivation point
y2 = f(x2) # result at the other, close point
approximate_derivative = (y2-y1)/(x2-x1)
print(approximate_derivative)

plt.plot(x, y)

plt.show()
