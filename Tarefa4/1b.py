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

    print("Linha", i+1, ": |diagonal| =", diagonal, " soma dos outros =", soma)

    if diagonal > soma:
        print("A linha", i+1, "é diagonalmente dominante.")
    else:
        print("A linha", i+1, "NÃO é diagonalmente dominante.")

# Chute Inicial
x_old = np.ones(n)

# Alocação de Memória
k = 0
x_new = np.zeros(n)
Epest = np.linspace(100, 100, n)
maxit = 100

erros = []
iteracoes = []

print("\nIterações:")

while (np.max(Epest) > Eppara and k < maxit):
    
    for i in range(0, n):

        soma1 = 0
        soma2 = 0

        for j in range(0, n):

            if j < i:
                soma1 += A[i, j]*x_new[j]
            
            elif j > i:
                soma2 += A[i, j]*x_old[j]                
    
        x_new[i] = 1/A[i, i]*(b[i] - soma1 - soma2)
    
    Epest = np.abs((x_new - x_old)/x_new)*100

    k += 1
    erros.append(np.max(Epest))
    iteracoes.append(k)

    print("Iteração:", k)
    print("x =", x_new[0], " y =", x_new[1], " z =", x_new[2])
    print("Erro máximo =", np.max(Epest), "%\n")
    
    x_old = x_new.copy()

print("Resultado final:")
print("x =", x_new[0])
print("y =", x_new[1])
print("z =", x_new[2])

print("\nNúmero de iterações:", k)
print("Erro estimado final:", np.max(Epest), "%")

if np.max(Epest) <= Eppara:
    print("\nConclusão: o método convergiu.")
else:
    print("\nConclusão: o método não convergiu dentro do número máximo de iterações.")

print("\nInterpretação:")
print("Leite desnatado =", x_new[0]*100, "g")
print("Farinha de soja =", x_new[1]*100, "g")
print("Whey =", x_new[2]*100, "g")

# Gráfico do erro
plt.plot(iteracoes, erros, marker='o')
plt.xlabel("Iterações")
plt.ylabel("Erro estimado máximo (%)")
plt.title("Convergência do Método de Gauss-Seidel")
plt.grid()
plt.show()