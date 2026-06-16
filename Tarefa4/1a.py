import numpy as np

A = np.array([[36, 4, 3],
              [5, 41, 6],
              [2, 7, 74]], dtype=float)

b = np.array([[39], [52], [83]], dtype=float)

A_original = A.copy()
b_original = b.copy()

Aum = np.hstack((A, b)) # Matriz Aumentada
n = len(b)

print("Matriz aumentada inicial:")
print(Aum)

# Eliminação Progressiva com Pivotamento
for i in range(n-1):

    maior = i
    for k in range(i+1, n):
        if abs(Aum[k, i]) > abs(Aum[maior, i]):
            maior = k

    if maior != i:
        linha = Aum[i].copy()
        Aum[i] = Aum[maior]
        Aum[maior] = linha
        print("\nTroca de linhas:")
        print(Aum)

    for j in range(i+1, n):
        fator = Aum[j, i]/Aum[i, i]
        Aum[j, i:n+1] = Aum[j, i:n+1] - fator*Aum[i, i:n+1]

    print("\nMatriz após etapa", i+1, "da eliminação:")
    print(Aum)

# Substituição Regressiva
x = np.zeros(n)

x[n-1] = Aum[n-1, n]/Aum[n-1, n-1]

for i in range(n-2, -1, -1):
    soma = 0
    for j in range(i+1, n):
        soma += Aum[i, j]*x[j]
    x[i] = (Aum[i, n] - soma)/Aum[i, i]

residuo = np.dot(A_original, x) - b_original.flatten()

print("\nSolução pelo método de Gauss com Pivotamento:")
print("x =", x[0])
print("y =", x[1])
print("z =", x[2])

print("\nResíduo A*x - b:")
print(residuo)

print("\nInterpretação:")
print("Leite desnatado =", x[0]*100, "g")
print("Farinha de soja =", x[1]*100, "g")
print("Whey =", x[2]*100, "g")