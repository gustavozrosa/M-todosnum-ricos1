import math

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

xi = 3
Eppara = 0.01
Epest = 100

while Epest > Eppara:
    xnovo = xi - f(xi)/df(xi)
    Epest = abs((xnovo - xi)/xnovo) * 100
    xi = xnovo

print(xnovo)