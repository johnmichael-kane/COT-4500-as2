import numpy as np
import math

def newtons_forward_method(x, f_x):
    # Calculate step size
    h = x[1] - x[0]

    # Calculate differences
    n = len(f_x)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = f_x

    for j in range(1, n):
        for i in range(n-j):
            diff_table[i, j] = diff_table[i+1, j-1] - diff_table[i, j-1]

    # Coefficients for the polynomial
    coefficients = [diff_table[0, 0]]  # f(a)
    for degree in range(1, n):
        coefficient = diff_table[0, degree] / (h**degree * math.factorial(degree))
        coefficients.append(coefficient)

    # Print the coefficients for polynomials of degree 1, 2, and 3
    for degree in range(1, 4):
        print(f"Polynomial of degree {degree}:")
        print(f"({', '.join([f'{coefficients[i]}' for i in range(degree + 1)])})\n")

def main():
    # Given data
    x = np.array([7.2, 7.4, 7.5, 7.6])
    f_x = np.array([23.5492, 25.3913, 26.8224, 27.4589])

    # Call the function
    newtons_forward_method(x, f_x)

# Instead of using if __name__ == "__main__":
main()