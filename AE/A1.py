import numpy as np
import math
import matplotlib.pyplot as plt

# função real
def f_real(x):
    return 1/(1-x)

# termo da série
def termo(x, n):
    return x**n

# valores de x
x_vals = [0.5, 0.8]

# erro de parada 
Eppara = 0.5 * 10**(-4)

for x in x_vals:

    soma = 0
    estimativa = []
    contador = []
    EPT = []
    EPEST = [100]

    v_old = 0
    i = 0

    real = f_real(x)

    Epest = 100  # inicial

    while Epest > Eppara:

        soma = soma + termo(x, i)
        v_new = soma

        # erro verdadeiro
        Ept = abs((real - soma)/real)*100

        # erro estimado
        if i > 0:
            Epest = abs((v_new - v_old)/v_new)*100
            EPEST.append(Epest)

        v_old = v_new

        EPT.append(Ept)
        estimativa.append(soma)
        contador.append(i)

        i += 1

    # gráfico estimativa
    plt.figure()
    plt.plot(contador, estimativa, 'or', label="Estimativa")
    plt.axhline(real, color='b', label="Valor real")
    plt.legend()
    plt.xlabel("numero de termos")
    plt.ylabel("valor")
    plt.title(f"x = {x}")
    plt.grid()

    # gráfico erros
    plt.figure()
    plt.plot(contador, EPT, 'ok', label="Ept")
    plt.plot(contador, EPEST, 'og', label="Epest")
    plt.legend()
    plt.xlabel("numero de termos")
    plt.ylabel("erro (%)")
    plt.title(f"x = {x}")
    plt.grid()

plt.show()