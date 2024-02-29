import numpy as np

# Data
x = [2, 5, 8, 10]
y = [3, 5, 7, 9]

# Matrix A
A = np.array(
[[ 1.,  0.,  0.,  0.],

 [ 3., 12.,  3.,  0.],

 [ 0.,  3., 10.,  2.],

 [ 0.,  0.,  0.,  1.]])

# Vector b
b = np.array(
[0.69369369, 0.61261261, 0.85585586])

# Solve for c (Spline coefficients)
c = np.linalg.solve(A, b)

print("Matrix A:", A)
print("Vector b:", b)
print("Spline coefficients (c):", c)
