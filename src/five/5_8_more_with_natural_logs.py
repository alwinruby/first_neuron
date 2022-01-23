import numpy as np

# below will give a runtime warning
# print(np.mean([1, 2, 3, -np.log(0)]))

print(-np.log(1e-7))

# Adding a very small value, one-tenth of a million, to the confidence at its far edge will
# insignificantly impact the result, but this method yields an additional 2 issues. First, in the case
# where the confidence value is 1
print(-np.log(1+1e-7))

# When the model is fully correct in a prediction and puts all the confidence in the correct label,
# loss becomes a negative value instead of being 0. The other problem here is shifting confidence
# towards 1, even if by a very small value. To prevent both issues, it’s better to clip values from both
# sides by the same number, 1e-7 in our case. That means that the lowest possible value will become
# 1e-7
print(-np.log(1-1e-7))