import numpy as np
def f(x):
    return 1 - np.exp(-x)
a = 0
b = 4
I_exato = 3 + np.exp(-4)
n_sig = 6
Eppara = 0.5 * 10**(2 - n_sig)
n = 1
Epest = 100
while Epest > Eppara:

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)

    I = h * (f(x[0]) + 2 * np.sum(f(x[1:n])) + f(x[n])) / 2

    Epest = abs((I_exato - I) / I_exato) * 100

    n += 1
print(f"n = {n-1}")
print(f"Integral = {I:.6f}")
print(f"Erro = {Epest:.8f}%")