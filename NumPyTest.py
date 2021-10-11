import numpy as np
from scipy import sparse

x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n{}".format(x))

# create a 2d NumPy array with a diagonal of ones, and zeros everywhere else
eye = np.eye(10)
print("NumPy array:\n{}".format(eye))

print("NumPy array:\n{}".format(np.random.randn(1000, 4)[:200]))
