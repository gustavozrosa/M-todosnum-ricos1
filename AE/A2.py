import math
import matplotlib.pyplot as plt

real = (math.pi**4)/90

soma = 0
i = 1

Eppara = 0.5 * 10**(-4)

Epest = 100
EPT = 100

v_old = 0

contador = []
valores_soma = []
valores_ept = []
valores_epest = []

while Epest > Eppara:

    soma = soma + 1/(i**4)
    v_new = soma

    # erro verdadeiro
    EPT = abs((real - soma)/real)*100

    # erro estimado
    if i > 1:
        Epest = abs((v_new - v_old)/v_new)*100

    v_old = v_new

    contador.append(i)
    valores_soma.append(soma)
    valores_ept.append(EPT)
    valores_epest.append(Epest)

    print("i =", i)
    print("soma =", soma)
    print("Ept =", EPT)
    print("Epest =", Epest)
    print("-------------------")

    i += 1

print("Numero de termos necessario:", i-1)

# gráfico da soma
plt.figure()
plt.plot(contador, valores_soma, 'ob')
plt.xlabel("numero de termos")
plt.ylabel("soma")
plt.title("Aproximacao da serie")
plt.grid()

# gráfico dos erros
plt.figure()
plt.plot(contador, valores_ept, 'ok', label="Ept")
plt.plot(contador, valores_epest, 'og', label="Epest")
plt.xlabel("numero de termos")
plt.ylabel("erro (%)")
plt.title("Erros da aproximacao")
plt.legend()
plt.grid()

plt.show()