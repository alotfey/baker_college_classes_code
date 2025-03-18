# Python Numpy Arrays and Operations

This README file provides the instructions and guidance for performing various array manipulations using Python's NumPy library.

## Tasks

### Array Creation and Properties

1. **Create a NumPy array** named `a` with shape `(3, 4)` and the following elements:
```
3  8  15  2
2  10  5  3
4  0   2  4
```

2. Determine the **shape** of array `a`.

3. Identify the **number of dimensions (`ndim`)** of array `a`.

4. Calculate the **length (`len`)** of array `a`.

5. Verify if the **`ndim` and `len`** can be derived from the shape property.

### Array Generation

6. Generate a **1D array** containing values from **2 through 5 inclusive**.

7. Create a NumPy array containing **10 equally spaced elements** from **2 to 5 inclusive**.

8. Generate a NumPy array filled with ones having shape `(4, 4)`.

9. Create an **identity matrix** of shape `(6, 6)`.

10. Construct the following array using a single Python/NumPy command:
```
1 0 0
0 2 0
0 0 3
```

### Random Array Generation

11. Refer to the docstring for `np.random.randn` and create a NumPy array with shape `(3, 5)` filled with random numbers from a standard normal distribution.

### Array Indexing and Slicing

12. Create the following array, named `a`:
```
2  7  12  0
3  9   3  4
4  0   1  3
```

13. Extract the **second row** from array `a`.

14. Extract the **third column** from array `a`.

### Advanced Array Construction

15. Construct the following arrays (ensure correct data types):
```
[[1, 1, 1, 1],
 [1, 1, 1, 1],
 [1, 1, 1, 2],
 [1, 6, 1, 1]]

[[0., 0., 0., 0., 0.],
 [2., 0., 0., 0., 0.],
 [0., 3., 0., 0., 0.],
 [0., 0., 4., 0., 0.],
 [0., 0., 0., 5., 0.],
 [0., 0., 0., 0., 6.]]
```

### Boolean Masking and Conditional Selection

16. Re-create the following array `a`:
```
2  7  12  0
3  9   3  4
4  0   1  3
```

17. Use the `>` operator to create a **boolean mask** indicating elements greater than 5.

18. Select and return **all elements greater than 5** from array `a`.

19. Modify array `a` by setting **all elements greater than 5** to the value **5**.

### Aggregations and Statistical Operations

20. Using array `a`:
```
2  7  12  0
3  9   3  4
4  0   1  3
```
Calculate and display:
- The **sum** of all elements.
- The sum of all **columns**.
- The sum of all **rows**.
- The **mean** of all elements.
- The **minimum** value in the array.
- The **maximum** value in the array.

---

Ensure to include both Python code and results for each task clearly in your notebook or script.

