import numpy as np

def f(x):
    return 1 - np.exp(-x)

a = 0
b = 4

I_exato = 3 + np.exp(-4)

n_sig = 6
Eppara = 0.5 * 10**(2 - n_sig)

n = 2
erro = 100

while erro > Eppara:

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)

    I = h/3 * (
        f(x[0])
        + 4*np.sum(f(x[1:n:2]))
        + 2*np.sum(f(x[2:n-1:2]))
        + f(x[n])
    )

    erro = abs((I_exato - I) / I_exato) * 100

    if erro > Eppara:
        n += 2

print(f"n = {n}")
print(f"Integral = {I:.6f}")
print(f"Erro = {erro:.8f}%")