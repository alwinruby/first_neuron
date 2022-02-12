import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(5))


def f(x):
    return 2 * x ** 2


y = f(x)  # Calculate function outputs for new function

print(x)
print(y)

print((y[1] - y[0]) / (x[1] - x[0]))

plt.plot(x, y)

plt.show()
