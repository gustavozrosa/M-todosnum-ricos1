import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Dados
R = 0.518
Pc = 4600
Tc = 191
T = -40 + 273.15
P = 65000
Vtanque = 3
a = 0.427 * R**2 * Tc**2.5 / Pc
b = 0.0866 * R * Tc / Pc
erro_max = 0.0001
V = R * T / P

erro = 100

while erro > erro_max:
    Vnovo = b + (R*T)/(P + a/(V*(V+b)))
    erro = abs((Vnovo - V)/Vnovo) * 100
    V = Vnovo

massa = Vtanque / V

print("V =", V)
print("Massa =", massa)