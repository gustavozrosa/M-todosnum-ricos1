import math
r = 2
L = 5
V = 8
n = 6
Eppara = 0.5 * 10**(2 - n)
def f(h):
    return V - (
        r**2 * math.acos((r - h) / r)
        - (r - h) * math.sqrt(2 * r * h - h**2)
    ) * L
delta = 0.001
h_old = (0.55 + 1.86) / 2
Epest = 100
k = 0
maxiter = 1000
while Epest > Eppara and k < maxiter:

    h_new = h_old - (
        delta * h_old * f(h_old)
        / (f(h_old + delta * h_old) - f(h_old))
    )

    Epest = abs((h_new - h_old) / h_new) * 100

    h_old = h_new
    k += 1
print(f"h = {h_old:.6f} m")
print(f"Epest = {Epest:.8f}%")
print(f"Iterações = {k}")