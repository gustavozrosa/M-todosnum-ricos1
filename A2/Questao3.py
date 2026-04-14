import numpy as np

# dados
L = 0.2
rho = 1.23
mu = 1.79e-5
D = 0.005
V = 40

# Reynolds
Re = (rho * V * D) / mu
print("Re =", Re)

# chute inicial de Blasius
f0 = 0.316 / (Re**0.25)
print("f inicial =", f0)

# critério de parada
eppara = 0.5 * 10**(-4)

# item a
eps = 0.0015e-3
f = f0
epest = 100

while epest > eppara:
    fnovo = 1 / (-2 * np.log10((eps/(3.7*D)) + (2.51/(Re*np.sqrt(f)))))**2
    epest = abs((fnovo - f)/fnovo) * 100
    f = fnovo

deltap = f * L * rho * V**2 / (2*D)

print("\nITEM A")
print("f =", f)
print("Delta p =", deltap, "Pa")

# item b
eps = 0.045e-3
f = f0
epest = 100

while epest > eppara:
    fnovo = 1 / (-2 * np.log10((eps/(3.7*D)) + (2.51/(Re*np.sqrt(f)))))**2
    epest = abs((fnovo - f)/fnovo) * 100
    f = fnovo

deltap = f * L * rho * V**2 / (2*D)

print("\nITEM B")
print("f =", f)
print("Delta p =", deltap, "Pa")