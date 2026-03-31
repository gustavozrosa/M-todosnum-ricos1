import math

def f(m):
    return math.sqrt((9.81*m)/0.25) * math.tanh(math.sqrt((9.81*0.25)/m)*4) - 36

xl = 140
xu = 150
Eppara = 0.01
Epest = 100
xr_old = 0
xex = 142.7376
i = 1

while Epest >= Eppara:
    xr = xu - (f(xu)*(xl - xu)) / (f(xl) - f(xu))

    if f(xl)*f(xr) < 0:
        xu = xr
    else:
        xl = xr

    if i > 1:
        Epest = abs((xr - xr_old)/xr)*100

    Ept = abs((xex - xr)/xex)*100

    print(i, xr, Epest, Ept)

    xr_old = xr
    i = i + 1

print("raiz =", xr)