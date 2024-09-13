import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2], [3, 4], [5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# Element-wise operations
arr = np.array([1, 2, 3, 4, 5])
arr_square = arr ** 2
arr_add = arr + 5

print("Squared Array:", arr_square)
print("Array after addition:", arr_add)


# Matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result = np.dot(matrix1, matrix2)

print("Matrix Multiplication:\n", result)

data = np.array([10, 20, 30, 40, 50])

mean = np.mean(data)      # Mean
median = np.median(data)  # Median
std_dev = np.std(data)    # Standard Deviation
variance = np.var(data)   # Variance

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)


x = np.linspace(0, 2 * np.pi, 100)

sin_values = np.sin(x)   # Sine of array elements
cos_values = np.cos(x)   # Cosine of array elements

print("Sine Values:\n", sin_values)
print("Cosine Values:\n", cos_values)

# Creating a large array
large_arr = np.random.rand(1000000)

# Element-wise multiplication using broadcasting
result = large_arr * 5

print("First 10 elements of result array:", result[:10])

# 3x3 matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Transpose of a matrix
matrix_transpose = np.transpose(matrix)

# Element-wise multiplication
elementwise_mul = matrix * matrix_transpose

print("Original Matrix:\n", matrix)
print("Transposed Matrix:\n", matrix_transpose)
print("Element-wise Multiplication:\n", elementwise_mul)
