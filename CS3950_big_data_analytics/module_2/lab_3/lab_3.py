# 1. Create an array with variable name “a” and the following contents (shape (3, 4)):
# 3 8 15 2
# 2 10 5 3
# 4 0 2 4
import numpy as np

a = np.array([[3, 8, 15, 2], [2, 10, 5, 3], [4, 0, 2, 4]])
print(f"shape of a: {a.shape}")
# 2. the array is 3x4
print(f"ndim of a: {a.ndim}")
# 3. the array is 2 dimensional
print(f"lenght of a: {len(a)}")
# 4. the array has 3 elements
# 5. Can you get the ndim and len from the shape?
# ndim from shape
print(f"ndim of a: {len(a.shape)}")
# len from shape
print(f"lenght of a: {a.shape[0]}")
# 6. Create a 1D array from 2 through 5 inclusive.
b = np.arange(2, 6)
print(f"1D array: {b}")
# 7. Make an array with 10 equally spaced elements between 2 and 5 inclusive.
c = np.linspace(2, 5, 10)
print(f"Array with 10 equally spaced elements: {c}")
# 8. Make an all-ones array shape (4, 4).
arr_ones = np.ones((4, 4))
print(f"All-ones array: {arr_ones}")
# 9. Make an identity array shape (6, 6).
arr_identity = np.eye(6)
print(f"Identity array: {arr_identity}")
# 10. Make this array with a single Python / numpy command:
# 1 0 0
# 0 2 0
# 0 0 3
arr_diag = np.diag([1, 2, 3])
print(f"Diagonal array: {arr_diag}")
# 11. Look at the docstring for np.random.randn. Make a shape (3, 5) array with
# random numbers from a standard normal distribution (a normal distribution
# with mean 0 and variance 1).

random_array = np.random.randn(3, 5)
print(random_array)
# 12. Create the following array, call this a:
# 2 7 12 0
# 3 9 3 4
# 4 0 1 3
arr2 = np.array([[2, 7, 12, 0], [3, 9, 3, 4], [4, 0, 1, 3]])
print(f"Array a: {arr2}")
# 13. Get the second row of a ([3 9 3 4]).
second_row = arr2[1]
print(f"Second row of a: {second_row}")
# 14. Get the third column of a ([12 3 1]).
third_column = arr2[:, 2]
print(f"Third column of a: {third_column}")
# 15. Create the following arrays (with correct data types):
# [[1, 1, 1, 1],
# [1, 1, 1, 1],
# [1, 1, 1, 2],
# [1, 6, 1, 1]]
# [[0., 0., 0., 0., 0.],
# [2., 0., 0., 0., 0.],
# [0., 3., 0., 0., 0.],
# [0., 0., 4., 0., 0.],
# [0., 0., 0., 5., 0.],
# [0., 0., 0., 0., 6.]]
arr3 = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 2], [1, 6, 1, 1]], dtype=int)
print(f"Array 1: {arr3}")
arr4 = np.array(
    [
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [2.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 3.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 4.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 5.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 6.0],
    ],
    dtype=float,
)
print(f"Array 2: {arr4}")
# 16. Create the following array a (same as before):
# 2 7 12 0
# 3 9 3 4
# 4 0 1 3
arr5 = np.array([[2, 7, 12, 0], [3, 9, 3, 4], [4, 0, 1, 3]])
print(f"Array a: {arr5}")
# 17. Use > to make a mask that is true where the elements are greater than 5, like
# this:
# False True True False
# False True False False
# False False False False
mask = arr5 > 5
print(f"Mask: {mask}")
# 18. Return all the elements in that are greater than 5.
elements_greater_than_5 = arr5[mask]
print(f"Elements greater than 5: {elements_greater_than_5}")
# 19. Set all the elements greater than 5 to be equal to 5.
arr5[mask] = 5
print(f"Array a after setting elements greater than 5 to 5: {arr5}")
# 20. Recall our array a:
# 2 7 12 0
# 3 9 3 4
# 4 0 1 3
# Sum of all the values
sum_all = a.sum()

# Sum of all the columns (axis=0 means summation down each column)
sum_cols = a.sum(axis=0)

# Sum of all the rows (axis=1 means summation across each row)
sum_rows = a.sum(axis=1)

# Mean
mean_val = a.mean()

# Minimum
min_val = a.min()

# Maximum
max_val = a.max()

# Print the results
print("Sum of all the values:", sum_all)

print("Sum of all the columns:", sum_cols)

print("Sum of all the rows:", sum_rows)

print("Mean:", mean_val)

print("Minimum:", min_val)

print("Maximum:", max_val)
