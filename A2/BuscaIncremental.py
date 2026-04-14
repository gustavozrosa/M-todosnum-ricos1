import numpy as np

def f(x):
    return np.sin(4*x) + np.cos(5*x) + 1/x

x = 0.1
passo = 0.01

while x < 2*np.pi:
    if f(x) * f(x + passo) < 0:
        print("Raiz entre:", x, "e", x + passo)
    x = x + passo