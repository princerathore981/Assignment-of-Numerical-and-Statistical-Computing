import numpy as np

x = [0, 1, 2, 3]
y = [1, 2, 4, 8]

n = len(x)
diff = np.zeros((n, n))
diff[:,0] = y

for j in range(1, n):
    for i in range(n-j):
        diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

value = 1.5
h = x[1] - x[0]
p = (value - x[0]) / h

result = y[0]
term = 1

for i in range(1, n):
    term *= (p - i + 1) / i
    result += term * diff[0][i]

print("Interpolated value:", result)
