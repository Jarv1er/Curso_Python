# Conjetura de Collattz

num = int(input("Inserta un numero: "))
result = ""

if num < 1:
    print("El numero insertado debe ser positivo")

while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1

    result += str(num)
    result += "\n"

print(result)


    