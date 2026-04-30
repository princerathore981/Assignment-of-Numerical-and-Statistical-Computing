def newton_backward(x, y, xp):
    n = len(x)
    diff = [y.copy()]

    for i in range(1, n):
        temp = []
        for j in range(n - i):
            temp.append(diff[i-1][j+1] - diff[i-1][j])
        diff.append(temp)

    h = x[1] - x[0]
    p = (xp - x[-1]) / h

    result = y[-1]
    fact = 1
    p_term = 1

    for i in range(1, n):
        fact *= i
        p_term *= (p + i - 1)
        result += (p_term * diff[i][-1]) / fact

    return result
