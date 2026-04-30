import numpy as np

def gauss_elimination(A, B):
    n = len(B)

    for i in range(n):
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] -= ratio * A[i][k]
            B[j] -= ratio * B[i]

    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = B[i]
        for j in range(i+1, n):
            X[i] -= A[i][j] * X[j]
        X[i] /= A[i][i]

    return X
