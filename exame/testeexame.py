import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#dados
Pc = 4600
Tc = 191
Vtanque = 3
T = -40+273.15
P = 65000
erro_max = 0.0001
erro = 100
R = 0.518
a = 0.427 * R**2 * Tc**2.5 / Pc
b = 0.0866*R*Tc/Pc
V = R*T/P
while erro > erro_max:
    V_novo = b + (R*T)/(P + a/(V*(V+b)))
    erro = abs((V_novo - V)/V_novo) *100
    V = V_novo
massa = Vtanque/V
print("V=", V)
print("massa=", massa)  