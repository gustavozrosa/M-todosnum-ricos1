import math
import matplotlib.pyplot as plt

# ============================================================
# EXERCÍCIO 2
# Aproximação da série:
# sum(1 / i^4), i = 1 até n
# que converge para:
# pi^4 / 90
# ============================================================

# Valor real da série infinita
real = (math.pi**4) / 90

# Critério de parada para 6 algarismos significativos
# Es = 0.5 * 10^(2-n)%
# Para n = 6:
# Es = 0.5 * 10^(-4) %
Eppara = 0.5 * 10**(-4)

# Inicializações
soma = 0
i = 1
v_old = 0
Epest = float("inf")

contador = []
valores_soma = []
valores_ept = []
valores_epest = []

while Epest > Eppara:
    soma += 1 / (i**4)
    v_new = soma

    # Erro relativo percentual verdadeiro
    Ept = abs((real - v_new) / real) * 100

    # Erro relativo percentual estimado
    # Só existe a partir da segunda aproximação
    if i == 1:
        Epest_plot = None
    else:
        Epest = abs((v_new - v_old) / v_new) * 100
        Epest_plot = Epest

    contador.append(i)
    valores_soma.append(v_new)
    valores_ept.append(Ept)
    valores_epest.append(Epest_plot)

    v_old = v_new
    i += 1

# ----------------------------
# Impressão dos resultados
# ----------------------------
print("N\tSoma\t\t\tEpt (%)\t\tEpest (%)")
for k in range(len(contador)):
    epest_str = "---" if valores_epest[k] is None else f"{valores_epest[k]:.10f}"
    print(f"{contador[k]}\t{valores_soma[k]:.10f}\t{valores_ept[k]:.10f}\t{epest_str}")

print(f"\nNúmero de termos necessário: {contador[-1]}")
print(f"Valor aproximado final = {valores_soma[-1]:.10f}")
print(f"Valor real             = {real:.10f}")
print(f"Ept final (%)          = {valores_ept[-1]:.10f}")
if valores_epest[-1] is not None:
    print(f"Epest final (%)        = {valores_epest[-1]:.10f}")

# ----------------------------
# Gráfico da soma
# ----------------------------
plt.figure()
plt.plot(contador, valores_soma, 'ob', label="Soma parcial")
plt.axhline(real, color='r', label="Valor real")
plt.xlabel("Número de termos")
plt.ylabel("Soma")
plt.title("Aproximação da série infinita")
plt.legend()
plt.grid()

# ----------------------------
# Gráfico dos erros
# ----------------------------
contador_epest = [contador[j] for j in range(len(valores_epest)) if valores_epest[j] is not None]
epest_validos = [valores_epest[j] for j in range(len(valores_epest)) if valores_epest[j] is not None]

plt.figure()
plt.plot(contador, valores_ept, 'ok', label="Ept")
plt.plot(contador_epest, epest_validos, 'og', label="Epest")
plt.xlabel("Número de termos")
plt.ylabel("Erro (%)")
plt.title("Erros da aproximação")
plt.legend()
plt.grid()

plt.show()