import math
x1 = int(input("Digite o valor x do plano01:"))
y1 = int(input("Digite o valor y do plano01:"))
x2 = int(input("Digite o valor x do plano02:"))
y2 = int(input("Digite o valor y do plano02:"))

distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

if distancia >= 10:
    print("longe")
else:
    print("perto")
