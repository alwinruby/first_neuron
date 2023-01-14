import matplotlib.pyplot as plt
import nnfs
from nnfs.datasets import sine_data


nnfs.init()
X_test, y_test = sine_data()

plt.plot(X_test, y_test)
plt.show()

