import numpy as np
import matplotlib.pyplot as plt

A = np.array([[36, 4, 3],
              [5, 41, 6],
              [2, 7, 74]], dtype=float)

b = np.array([39, 52, 83], dtype=float)

n = len(b)

na = 12
Eppara = 0.5*10**(2 - na)

print("Critério de parada Eppara =", Eppara)

# Verificação da diagonal dominante
print("\nVerificação da diagonal dominante:")

for i in range(n):

    diagonal = abs(A[i, i])

    soma = 0

    for j in range(n):

        if j != i:
            soma += abs(A[i, j])

    print("Linha", i+1)

    print("|Diagonal| =", diagonal)
    print("Soma dos outros =", soma)

    if diagonal > soma:
        print("A linha é diagonalmente dominante.\n")
    else:
        print("A linha NÃO é diagonalmente dominante.\n")

# Chute inicial
x_old = np.ones(n)

# Alocação de memória
x_new = np.zeros(n)

Epest = np.linspace(100, 100, n)

k = 0
maxit = 100

erros = []
iteracoes = []

print("Iterações:\n")

while (np.max(Epest) > Eppara and k < maxit):

    for i in range(n):

        soma = 0

        for j in range(n):

            if j != i:
                soma += A[i, j]*x_old[j]

        x_new[i] = (b[i] - soma)/A[i, i]

    Epest = np.abs((x_new - x_old)/x_new)*100

    k += 1

    erros.append(np.max(Epest))
    iteracoes.append(k)

    print("Iteração:", k)
    print("x =", x_new[0],
          " y =", x_new[1],
          " z =", x_new[2])

    print("Erro máximo =", np.max(Epest), "%\n")

    x_old = x_new.copy()

print("Resultado final:")
print("x =", x_new[0])
print("y =", x_new[1])
print("z =", x_new[2])

print("\nNúmero de iterações:", k)

print("Erro estimado final =", np.max(Epest), "%")

if np.max(Epest) <= Eppara:
    print("\nConclusão: o método convergiu.")
else:
    print("\nConclusão: o método não convergiu.")

print("\nInterpretação:")

print("Leite desnatado =", x_new[0]*100, "g")
print("Farinha de soja =", x_new[1]*100, "g")
print("Whey =", x_new[2]*100, "g")

# Gráfico do erro
plt.plot(iteracoes, erros, marker='o')

plt.xlabel("Iterações")

plt.ylabel("Erro estimado máximo (%)")

plt.title("Convergência do Método de Jacobi")

plt.grid()

plt.show()