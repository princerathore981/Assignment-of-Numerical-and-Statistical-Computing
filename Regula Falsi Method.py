def f(x):
    return x**3 - x - 2

a = 1
b = 2
tol = 0.0001

while True:
    c = (a*f(b) - b*f(a)) / (f(b) - f(a))
    if abs(f(c)) < tol:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

print("Root:", c)
