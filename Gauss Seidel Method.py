import numpy as np

def gauss_seidel(A, B, tol=1e-6, max_iter=100):
    n = len(B)
    X = np.zeros(n)

    for _ in range(max_iter):
        X_new = np.copy(X)

        for i in range(n):
            s1 = sum(A[i][j]*X_new[j] for j in range(i))
            s2 = sum(A[i][j]*X[j] for j in range(i+1, n))
            X_new[i] = (B[i] - s1 - s2) / A[i][i]

        if np.allclose(X, X_new, atol=tol):
            return X_new
        X = X_new

    return X
