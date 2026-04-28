import math
x = 0.3*math.pi
eppara = 0.5 * 10**(-6)
soma = 0
soma_antiga = 0
epest = 100
n = 0
while epest > eppara:
    termo = ((-1)**n) * (x**(2*n)) / math.factorial(2*n)
    soma_antiga = soma
    soma = soma + termo
    n = n + 1
    if n > 1:
        epest = abs((soma - soma_antiga) / soma) * 100

print("Aproximação:", soma)
print("Erro percentual estimado:", epest, "%")
print("Número de termos necessários:", n)