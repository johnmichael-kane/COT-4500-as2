import numpy as np
import math

x = np.array([7.2, 7.4, 7.5, 7.6])
f_x = np.array([23.5492, 25.3913, 26.8224, 27.4589])

#Create a diff table:
n=len(x)
diff_table=np.zeros((n, n))
diff_table[:, 0] = f_x

for j in range(1, n):
    for i in range(n-j):
        diff_table[i, j] = (diff_table[i+1, j-1] - diff_table[i, j-1]) / (x[i + j] - x[i])

#c is the coefficients
#maybe move this code around for a bit
c = [diff_table[0, i] for i in range(n)]

d1, d2, d3=c[1:]


def main():
  for i in c[1:]: print(i)

if __name__ == "__main__":
  main()
