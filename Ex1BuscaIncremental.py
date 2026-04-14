import math
import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# FUNÇÃO DO PROBLEMA
# ============================================================
def f(x):
    return np.sin(10 * x) + np.cos(3 * x)


# ============================================================
# BUSCA INCREMENTAL
# ============================================================
def busca_incremental(func, x_inicial, x_final, passo):
    """
    Realiza busca incremental para encontrar subintervalos
    onde ocorre mudança de sinal.

    Retorna:
        lista de tuplas (xl, xu)
    """
    intervalos = []

    xl = x_inicial
    xu = xl + passo

    print("\n" + "=" * 75)
    print("   xl         xu        f(xl)       f(xu)      f(xl)*f(xu)")
    print("=" * 75)

    while xu <= x_final:
        fxl = math.sin(10 * xl) + math.cos(3 * xl)
        fxu = math.sin(10 * xu) + math.cos(3 * xu)
        produto = fxl * fxu

        print(f"{xl:8.3f}   {xu:8.3f}   {fxl:10.6f}   {fxu:10.6f}   {produto:12.6f}")

        if produto < 0:
            intervalos.append((xl, xu))

        xl = xu
        xu = xl + passo

    print("=" * 75)
    return intervalos


# ============================================================
# GRÁFICO
# ============================================================
def plotar_grafico(func, x_inicial, x_final, intervalos):
    """
    Plota o gráfico da função e destaca os intervalos
    onde ocorre mudança de sinal.
    """
    x = np.linspace(x_inicial, x_final, 1000)
    y = func(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x) = sen(10x) + cos(3x)')
    plt.axhline(0, linestyle='--', linewidth=1)

    # destacar os intervalos com mudança de sinal
    for i, (xl, xu) in enumerate(intervalos):
        plt.axvline(xl, linestyle='--', linewidth=1)
        plt.axvline(xu, linestyle='--', linewidth=1)

        plt.scatter([xl, xu],
                    [math.sin(10 * xl) + math.cos(3 * xl),
                     math.sin(10 * xu) + math.cos(3 * xu)],
                    zorder=3)

        # só coloca legenda no primeiro para não repetir
        if i == 0:
            plt.axvspan(xl, xu, alpha=0.2, label='Intervalo com mudança de sinal')
        else:
            plt.axvspan(xl, xu, alpha=0.2)

    plt.title("Busca Incremental - Mudança de sinal da função")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================
def main():
    x_inicio = 3
    x_fim = 6
    passo = 0.1

    print("\nBUSCA INCREMENTAL COM VISUALIZAÇÃO GRÁFICA")
    print(f"Função: f(x) = sen(10x) + cos(3x)")
    print(f"Intervalo analisado: [{x_inicio}, {x_fim}]")
    print(f"Passo adotado: {passo}")

    intervalos = busca_incremental(f, x_inicio, x_fim, passo)

    print("\nSUBINTERVALOS ONDE f(xl) * f(xu) < 0:")
    print("-" * 50)

    if len(intervalos) == 0:
        print("Nenhum intervalo com mudança de sinal foi encontrado.")
    else:
        for i, (xl, xu) in enumerate(intervalos, start=1):
            print(f"Raiz {i}: entre {xl:.3f} e {xu:.3f}")

    plotar_grafico(f, x_inicio, x_fim, intervalos)


# ============================================================
# EXECUÇÃO
# ============================================================
if __name__ == "__main__":
    main()