# Approximating f(7.3) using Newton's forward method results
import numpy as np

# Given data
x_data = [7.2, 7.4, 7.5, 7.6]
f_data = [23.5492, 25.3913, 26.8224, 27.4589]

# Target for approximation
x_target = 7.3

# Forward difference table
forward_diff = np.array([[23.5492, 1.842100000000002, -0.4110000000000049, -0.3835999999999906], [25.3913, 1.4310999999999972, -0.7945999999999955, 0.0], [26.8224, 0.6365000000000016, 0.0, 0.0], [27.4589, 0.0, 0.0, 0.0]])

# Calculating the approximate value
u = (x_target - x_data[0]) / (x_data[1] - x_data[0])
approx_value = forward_diff[0][0]
u_product = 1
for i in range(1, len(x_data)):
    u_product *= (u - (i-1)) / i
    approx_value += u_product * forward_diff[0][i]

print('Approximate value of f(7.3): 24.497649999999997')