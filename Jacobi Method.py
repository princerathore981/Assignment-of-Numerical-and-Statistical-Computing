import numpy as np

def jacobi(A, B, tol=1e-6, max_iter=100):
    n = len(B)
    X = np.zeros(n)

    for _ in range(max_iter):
        X_new = np.zeros(n)
        for i in range(n):
            s = sum(A[i][j]*X[j] for j in range(n) if j != i)
            X_new[i] = (B[i] - s) / A[i][i]

        if np.allclose(X, X_new, atol=tol):
            return X_new
        X = X_new

    return X
