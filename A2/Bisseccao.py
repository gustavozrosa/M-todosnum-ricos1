import numpy as np

def f(x):
    return np.sin(4*x) + np.cos(5*x) + 1/x

xl = 2.69
xu = 2.70
eppara = 0.5 * 10**(-4)

epest = 100
xr_old = 0

while epest > eppara:
    xr = (xl + xu) / 2

    if f(xl) * f(xr) < 0:
        xu = xr
    else:
        xl = xr

    if xr != 0:
        epest = abs((xr - xr_old) / xr) * 100

    xr_old = xr

print("Raiz =", xr)