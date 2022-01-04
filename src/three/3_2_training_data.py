# function that can create non-linear data

from nnfs.datasets import spiral_data

import numpy as np
import nnfs

nnfs.init()

# The nnfs.init() does three things: it sets the random seed to 0 (by the default), creates a
# float32 dtype default, and overrides the original dot product from NumPy. All of these are meant
# to ensure repeatable results for following along.
# The spiral_data function allows us to create a dataset with as many classes as we want. The
# function has parameters to choose the number of classes and the number of points/observations
# per class in the resulting non-linear dataset.

import matplotlib.pyplot as plt

X, y = spiral_data(samples=100, classes=3)
plt.scatter(X[:, 0], X[:, 1])

plt.show()

plt.scatter(X[:, 0], X[:, 1], c=y, cmap='brg')
plt.show()

# Keep in mind that the neural network will not be aware of the color differences as the data have no
# class encodings. This is only made as an instruction for the reader. In the data above, each dot is
# the feature, and its coordinates are the samples that form the dataset. The “classification” for that
# dot has to do with which spiral it is a part of, depicted by blue, green, or red color in the previous
# image. These colors would then be assigned a class number for the model to fit to, like 0, 1, and 2.