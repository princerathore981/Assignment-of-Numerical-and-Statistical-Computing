def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

x = 1.5
tol = 0.0001

while True:
    x_new = x - f(x)/df(x)
    if abs(x_new - x) < tol:
        break
    x = x_new

print("Root:", x_new)
