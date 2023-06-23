# Software que permita contar las cantidad de veces que aparece 
# la letra a en una frase solicitada al usuario

frase = input("Escribe una frase: ")

count = 0
for f in frase:
    if f == "a":
        count += 1

print(count)

