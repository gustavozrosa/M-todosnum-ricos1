import numpy as np
import matplotlib.pyplot as plt

sistemas = [
    {
        "nome": "Conjunto 1",
        "A": np.array([[8, 3, 1],
                       [-6, 0, 7],
                       [2, 4, -1]], dtype=float),
        "b": np.array([12, 1, 5], dtype=float)
    },
    {
        "nome": "Conjunto 2",
        "A": np.array([[1, 1, 5],
                       [-1, 4, -1],
                       [3, 1, -1]], dtype=float),
        "b": np.array([7, 4, 3], dtype=float)
    },
    {
        "nome": "Conjunto 3",
        "A": np.array([[-7, 3, 5],
                       [-2, 4, -5],
                       [0, 2, -1]], dtype=float),
        "b": np.array([7, -3, 1], dtype=float)
    }
]

na = 6
Eppara = 0.5*10**(2 - na)
maxit = 20

for sistema in sistemas:

    print("\n==============================")
    print(sistema["nome"])
    print("==============================")

    A = sistema["A"]
    b = sistema["b"]

    n = len(b)

    print("\nMatriz A:")
    print(A)

    print("\nVetor b:")
    print(b)

    print("\nVerificação da diagonal dominante:")

    for i in range(n):

        diagonal = abs(A[i, i])
        soma = 0

        for j in range(n):
            if j != i:
                soma += abs(A[i, j])

        print("Linha", i+1, ": |diagonal| =", diagonal, " soma dos outros =", soma)

        if diagonal > soma:
            print("A linha", i+1, "é diagonalmente dominante.")
        else:
            print("A linha", i+1, "NÃO é diagonalmente dominante.")

    if np.any(np.diag(A) == 0):
        print("\nConclusão:")
        print("Este sistema possui zero na diagonal principal.")
        print("Logo, não é possível aplicar Gauss-Seidel diretamente nessa ordem, pois ocorreria divisão por zero.")
        continue

    x_old = np.ones(n)
    x_new = np.zeros(n)
    Epest = np.linspace(100, 100, n)

    k = 0

    erros = []
    iteracoes = []

    print("\nIterações:")

    while (np.max(Epest) > Eppara and k < maxit):

        for i in range(n):

            soma1 = 0
            soma2 = 0

            for j in range(n):

                if j < i:
                    soma1 += A[i, j]*x_new[j]

                elif j > i:
                    soma2 += A[i, j]*x_old[j]

            x_new[i] = (b[i] - soma1 - soma2)/A[i, i]

        Epest = np.abs((x_new - x_old)/x_new)*100

        k += 1

        erros.append(np.max(Epest))
        iteracoes.append(k)

        print("Iteração:", k)
        print("x =", x_new[0], " y =", x_new[1], " z =", x_new[2])
        print("Erro máximo =", np.max(Epest), "%\n")

        x_old = x_new.copy()

    print("Resultado após", k, "iterações:")
    print(x_new)

    print("Erro final:", np.max(Epest), "%")

    if np.max(Epest) <= Eppara:
        print("\nConclusão: o método convergiu.")
    else:
        print("\nConclusão: o método não convergiu dentro do número máximo de iterações.")

    plt.plot(iteracoes, erros, marker='o')
    plt.xlabel("Iterações")
    plt.ylabel("Erro estimado máximo (%)")
    plt.title("Erro estimado - " + sistema["nome"])
    plt.grid()
    plt.show()