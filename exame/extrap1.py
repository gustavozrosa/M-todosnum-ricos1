import math
def f(x):
    return 2*x*math.exp(-x**2)
a = 0
b = 2
R = (math.sqrt(5) - 1)/2
erro = 1e-6
while (b - a) > erro:

    x1 = b - R*(b - a)
    x2 = a + R*(b - a)

    if f(x1) > f(x2):
        b = x2
    else:
        a = x1
x = (a + b)/2
print(f"x = {x:.6f}")