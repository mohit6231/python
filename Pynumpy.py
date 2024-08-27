import numpy as np

array = np.zeros((3, 4), dtype=int)
print(array)

array = np.ones((3, 4), dtype=int)
print(array)

array = np.random.random((3, 4))
print(array > 0.2)
print(array[array > 0.2])


array = np.array([1, 2, 3])
print(array)
