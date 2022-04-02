import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

starting_learning_rate = 1.
learning_rate_decay = 0.1
step = 1
learning_rate = starting_learning_rate * \
(1. / (1 + learning_rate_decay * step))
print(learning_rate)

