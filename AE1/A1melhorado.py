import matplotlib.pyplot as plt

# ============================================================
# EXERCÍCIO 1
# Aproximação da função f(x) = 1 / (1 - x)
# usando a série geométrica:
# 1 + x + x^2 + x^3 + ... = sum(x^n), para |x| < 1
# ============================================================

# Função real
def f_real(x):
    return 1 / (1 - x)

# Termo n da série
def termo_serie(x, n):
    return x**n

# Valores de x pedidos para análise
x_vals = [0.5, 0.8]

# Critério de parada para 6 algarismos significativos
# Fórmula clássica em porcentagem:
# Es = 0.5 * 10^(2-n)%
# Para n = 6:
# Es = 0.5 * 10^(-4) %
Eppara = 0.5 * 10**(-4)

for x in x_vals:
    soma = 0
    i = 0
    real = f_real(x)

    contador = []
    estimativas = []
    erros_verdadeiros = []
    erros_estimados = []

    v_old = 0
    Epest = float("inf")  # começa infinito para entrar no laço

    while Epest > Eppara:
        soma += termo_serie(x, i)
        v_new = soma

        # Erro relativo percentual verdadeiro
        Ept = abs((real - v_new) / real) * 100

        # Erro relativo percentual estimado
        # Só existe a partir da segunda aproximação
        if i == 0:
            Epest_plot = None
        else:
            Epest = abs((v_new - v_old) / v_new) * 100
            Epest_plot = Epest

        contador.append(i)
        estimativas.append(v_new)
        erros_verdadeiros.append(Ept)
        erros_estimados.append(Epest_plot)

        v_old = v_new
        i += 1

    # ----------------------------
    # Impressão dos resultados
    # ----------------------------
    print(f"\nResultados para x = {x}")
    print("N\tSoma\t\t\tEpt (%)\t\tEpest (%)")
    for k in range(len(contador)):
        epest_str = "---" if erros_estimados[k] is None else f"{erros_estimados[k]:.10f}"
        print(f"{contador[k]}\t{estimativas[k]:.10f}\t{erros_verdadeiros[k]:.10f}\t{epest_str}")

    print(f"\nNúmero de termos necessários para x = {x}: {contador[-1] + 1}")
    print(f"Valor aproximado final = {estimativas[-1]:.10f}")
    print(f"Valor real            = {real:.10f}")
    print(f"Ept final (%)         = {erros_verdadeiros[-1]:.10f}")
    if erros_estimados[-1] is not None:
        print(f"Epest final (%)       = {erros_estimados[-1]:.10f}")

    # ----------------------------
    # Gráfico da estimativa
    # ----------------------------
    plt.figure()
    plt.plot(contador, estimativas, 'or', label="Estimativa")
    plt.axhline(real, color='b', label="Valor real")
    plt.xlabel("Número de termos")
    plt.ylabel("Valor")
    plt.title(f"Aproximação da série para x = {x}")
    plt.legend()
    plt.grid()

    # ----------------------------
    # Gráfico dos erros
    # ----------------------------
    contador_epest = [contador[j] for j in range(len(erros_estimados)) if erros_estimados[j] is not None]
    epest_validos = [erros_estimados[j] for j in range(len(erros_estimados)) if erros_estimados[j] is not None]

    plt.figure()
    plt.plot(contador, erros_verdadeiros, 'ok', label="Ept")
    plt.plot(contador_epest, epest_validos, 'og', label="Epest")
    plt.xlabel("Número de termos")
    plt.ylabel("Erro (%)")
    plt.title(f"Erros da aproximação para x = {x}")
    plt.legend()
    plt.grid()

plt.show()