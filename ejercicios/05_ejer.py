# Software que permita obtener el número de cifras que contiene un número entero

n = int(input("Escribe un numero: "))
cifras = 0

while n > 0:
    n = n // 10
    cifras += 1

print(f"El numero tiene {cifras} cifras")
