import numpy as np
import pandas as pd

# Created a one-dimensional NumPy array named arr1 with values from 1 to 10.
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Print the first element, the last element, and the fifth element of arr1.
print(f"First-last-fifth: {arr1[0]} {arr1[-1]} {arr1[4]}")
print()


# Created a two-dimensional NumPy array named arr2 with shape (3,3) containing values from 1 to 9.
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
# Print the first row of arr2.
print(f"First row: {arr2[0, :]}")
print()
# Print the second column of arr2.
print(f"Second column: {arr2[:, 1]}")
print()
# Use slicing to create a sub-array containing the first two rows and the first two columns of arr2.
print(f"Sub-array: \n{arr2[:2, :2]}")
print()

# Using the array arr2 from Task 2, transposed the array and store it in a new variable arr2_transposed.
arr2_transposed = arr2.transpose()
# Print both arr2 and arr2_transposed to see the difference.
print(f"Normal: \n{arr2}")
print(f"Transposed: \n{arr2_transposed}")

# Created two one-dimensional arrays a and b, where a = [1, 2, 3, 4, 5] and b = [5, 4, 3, 2, 1].
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
#  Add a and b using both the + operator and np.add().
print(f"Operator: {a + b} \n np.add(): {np.add(a, b)}")
#  Subtract b from a using both the - operator and np.subtract().
print(f"Operator: {b - a } \n np.subtract(): {np.subtract(b, a)}")
#  Multiply a and b using both the * operator and np.multiply().
print(f"Operator: {a * b } \n np.multiply(): { np.multiply(a, b)}")
#  Divide a by b using both the / operator and np.divide().
print(f"Operator: {a / b } \n np.divide(): {np.divide(a, b)}")
#  Calculate the remainder when a is divided by b using both the % operator and
# np.remainder().
print(f"Operator: {a % b } \n np.remainder(): {np.remainder(a, b)}")
print()
# Use np.sqrt() to compute the square root of each element in array a.
print(f"np.sqrt(): {np.sqrt(a)}")
print()
# Use np.exp() to compute the exponential of each element in array a.
print(f"np.exp(): {np.exp(a)}")
print()
# Use np.log() to compute the natural logarithm of each element in array b (make sure there are no zero
# values in b).
print(f"np.log(): {np.log(b)}")
print()
