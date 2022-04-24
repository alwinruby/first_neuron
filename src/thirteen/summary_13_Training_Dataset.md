# Training Dataset



Preprocessing - Neural networks usually perform best on data consisting of numbers in a range of 0 to 1 or -1 to
1, with the latter being preferable. Centering data on the value of 0 can help with model training
as it attenuates weight biasing in some direction. Models can work fine with data in the range of 0
to 1 in most cases, but sometimes we’re going to need to rescale them to a range of -1 to 1 to get
training to behave or achieve better results.


There are many terms related to data preprocessing: standardization, scaling, variance scaling,
mean removal, non-linear transformations, scaling to outliers, etc


In cases where we do not have many training samples, we could use data augmentation. One
easy way to understand augmentation is in the case of images. Let’s imagine that our model’s goal
is to detect rotten fruits — apples, for example. We will take a photo of an apple from different
angles and predict whether it’s rotten. We should get more pictures in this case, but let’s assume
that we cannot. What we could do is to take photos that we have, rotate, crop, and save those as
worthy data too. This way, we have added more samples to the dataset, which can help with model
generalization. In general, if we use augmentation, then it’s only useful if the augmentations that
we make are similar to variations that we could see in reality. For example, we may refrain from
using a rotation when creating a model to detect road signs as they are not being rotated in reallife
scenarios (in most cases, anyway).

The case of a rotated road sign, however, is one you better consider if you’re making a self-driving car. Just because a bolt came loose on a stop sign, flipping
it over, doesn’t mean you no longer need to stop there!

How many samples do we need to train the model? There is no single answer to this question —
one model might require just a few per class, and another may require a few million or billion.
Usually, a few thousand per class will be necessary, and a few tens of thousands should be
preferable to start. The difference depends on the data complexity and model size. If the model
has to predict sensor data with 2 simple classes, for example, if an image contains a dark area or
does not, hundreds of samples per class might be enough. To train on data with many features and
several classes, tens of thousands of samples are what you should start with. If you’re attempting
to train a chatbot the intricacies of written language, then you’re going to likely want at least
millions of samples.
Supplement