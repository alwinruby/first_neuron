# To train, neural networks tend to receive data in batches
# inputs = [1, 2, 3, 2.5]
# Here, the [1, 2, 3, 2.5] data are somehow meaningful and descriptive to the output we
# desire. Imagine each number as a value from a different sensor, from the example in chapter 1,
# all simultaneously. Each of these values is a feature observation datum, and together they form a
# feature set instance, also called an observation, or most commonly, a sample.

# Often, neural networks expect to take in many samples at a time for two reasons. One reason
# is that it’s faster to train in batches in parallel processing, and the other reason is that batches
# help with generalization during training. If you fit (perform a step of a training process) on one
# sample at a time, you’re highly likely to keep fitting to that individual sample, rather than slowly
# producing general tweaks to weights and biases that fit the entire dataset. Fitting or training in
# batches gives you a higher chance of making more meaningful changes to weights and biases. For
# the concept of fitment in batches rather than one sample at a time.


# A list of lists
from numpy import shape

# all samples, and are also referred to as feature set instances or
# observations.
inputs = [[1, 2, 3, 2.5], [2, 5, -1, 2], [-1.5, 2.7, 3.3, -0.8]]
print(shape(inputs))

# manage both matrices as lists of vectors and perform dot
# products on all of them in all combinations, resulting in a list of lists of outputs, or a matrix; this
# operation is called the matrix product.


