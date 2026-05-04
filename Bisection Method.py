def f(x):
    return x**3 - x - 2

a = 1
b = 2
tol = 0.0001

while (b - a) / 2 > tol:
    c = (a + b) / 2
    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

print("Root:", c)
