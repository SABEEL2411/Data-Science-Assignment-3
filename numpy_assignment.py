
import numpy as np


arr = np.arange(1, 21)
print("1D Array:", arr)


print("\nArray Statistics:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))


indices = np.where(arr > 10)
print("\nIndices of elements > 10:", indices)
print("Elements > 10:", arr[indices])


arr2d = np.arange(1, 17).reshape(4, 4)
print("\n2D Array:\n", arr2d)

# a. Transpose of the array
print("\nTranspose of Array:\n", arr2d.T)

# b. Row-wise and column-wise sums
print("\nRow-wise sum:", np.sum(arr2d, axis=1))
print("Column-wise sum:", np.sum(arr2d, axis=0))

A = np.random.randint(1, 21, (3, 3))
B = np.random.randint(1, 21, (3, 3))
print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

# a. Element-wise operations
print("\nAddition:\n", A + B)
print("Subtraction:\n", A - B)
print("Multiplication:\n", A * B)

# b. Dot product
print("\nDot Product:\n", np.dot(A, B))

arr_12 = np.arange(1, 13)
reshaped = arr_12.reshape(3, 4)
print("\nReshaped 3x4 Array:\n", reshaped)

# Slice first two rows and last two columns
sliced = reshaped[:2, -2:]
print("\nSliced Array (first 2 rows, last 2 columns):\n", sliced)

