import math
import matplotlib.pyplot as plt


# ============================================================
# PROBLEMA: BUNGEE JUMPING
# Objetivo:
# Determinar a massa m para que a velocidade após 4 s de queda
# seja igual a 36 m/s.
#
# Modelo:
# v(t) = sqrt((g*m)/cd) * tanh( sqrt((g*cd)/m) * t )
#
# Queremos resolver:
# f(m) = sqrt((g*m)/cd) * tanh( sqrt((g*cd)/m) * t ) - v_alvo = 0
# ============================================================


# -------------------------
# Dados do problema
# -------------------------
g = 9.81          # gravidade (m/s^2)
cd = 0.25         # coeficiente de arraste (kg/m)
t = 4.0           # tempo de queda (s)
v_alvo = 36.0     # velocidade desejada (m/s)


# -------------------------
# Função velocidade
# -------------------------
def velocidade(m):
    """
    Calcula a velocidade v(t) para uma massa m.

    Parâmetro:
        m (float): massa em kg

    Retorna:
        float: velocidade em m/s
    """
    termo1 = math.sqrt((g * m) / cd)
    termo2 = math.tanh(math.sqrt((g * cd) / m) * t)
    return termo1 * termo2


# -------------------------
# Função f(m)
# -------------------------
def f(m):
    """
    Função cuja raiz queremos encontrar.

    f(m) = velocidade(m) - v_alvo

    Parâmetro:
        m (float): massa em kg

    Retorna:
        float: valor da função
    """
    return velocidade(m) - v_alvo


# -------------------------
# Método da bisseção
# -------------------------
def bissecao(func, a, b, tolerancia=1e-6, max_iter=100):
    """
    Encontra uma raiz de func no intervalo [a, b]
    usando o método da bisseção.

    Parâmetros:
        func (callable): função a ser resolvida
        a (float): extremo esquerdo do intervalo
        b (float): extremo direito do intervalo
        tolerancia (float): critério de parada
        max_iter (int): número máximo de iterações

    Retorna:
        raiz (float): valor aproximado da raiz
        iteracoes (int): número de iterações realizadas
    """

    if func(a) * func(b) > 0:
        raise ValueError(
            "O método da bisseção exige que f(a) e f(b) tenham sinais opostos."
        )

    print("=" * 78)
    print("Iter |      a       |      b       |      xm      |    f(xm)")
    print("=" * 78)

    for i in range(1, max_iter + 1):
        xm = (a + b) / 2
        fxm = func(xm)

        print(f"{i:4d} | {a:12.6f} | {b:12.6f} | {xm:12.6f} | {fxm:10.6f}")

        # Critério de parada
        if abs(fxm) < tolerancia or abs(b - a) / 2 < tolerancia:
            print("=" * 78)
            return xm, i

        # Decide em qual subintervalo está a raiz
        if func(a) * fxm < 0:
            b = xm
        else:
            a = xm

    print("=" * 78)
    return xm, max_iter


# -------------------------
# Programa principal
# -------------------------
def main():
    print("\n" + "=" * 60)
    print("CÁLCULO DA MASSA NO PROBLEMA DE BUNGEE JUMPING")
    print("=" * 60)

    print(f"Gravidade (g): {g} m/s²")
    print(f"Coeficiente de arraste (cd): {cd} kg/m")
    print(f"Tempo (t): {t} s")
    print(f"Velocidade alvo: {v_alvo} m/s")

    # Intervalo inicial para procurar a raiz
    a = 40.0
    b = 200.0

    print(f"\nVerificando intervalo inicial: [{a}, {b}]")
    print(f"f({a}) = {f(a):.6f}")
    print(f"f({b}) = {f(b):.6f}")

    # Resolver por bisseção
    raiz, n_iter = bissecao(f, a, b, tolerancia=1e-6, max_iter=100)

    print("\nRESULTADO FINAL")
    print("-" * 30)
    print(f"Massa aproximada = {raiz:.6f} kg")
    print(f"Número de iterações = {n_iter}")
    print(f"Velocidade obtida = {velocidade(raiz):.6f} m/s")
    print(f"f(m) = {f(raiz):.10f}")

    # -------------------------
    # Geração do gráfico
    # -------------------------
    massas = []
    valores_f = []

    m_inicial = 100
    m_final = 200
    passo = 1

    m = m_inicial
    while m <= m_final:
        massas.append(m)
        valores_f.append(f(m))
        m += passo

    plt.figure(figsize=(8, 5))
    plt.plot(massas, valores_f, label="f(m)")
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.axvline(140, color="red", linestyle="--", linewidth=1)
    plt.axvline(150, color="red", linestyle="--", linewidth=1)

    plt.xlim(100, 200)
    plt.ylim(-1, 1)

    plt.xlabel("m (kg)")
    plt.ylabel("f(m)")
    plt.title("Estimativa gráfica da raiz")
    plt.legend()
    plt.grid(True)
    plt.show()


# -------------------------
# Execução do programa
# -------------------------
if __name__ == "__main__":
    main()