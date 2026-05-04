import numpy as np

A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], float)

B = np.array([8, -11, -3], float)

n = len(B)

# Forward elimination
for i in range(n):
    for j in range(i+1, n):
        ratio = A[j][i]/A[i][i]
        A[j] = A[j] - ratio*A[i]
        B[j] = B[j] - ratio*B[i]

# Back substitution
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (B[i] - sum(A[i][j]*x[j] for j in range(i+1, n))) / A[i][i]

print("Solution:", x)
