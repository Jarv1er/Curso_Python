# Software que dada una frase indique su longitud
# Con Split
frase = input("Escribe una frase: ")

new_frase = frase.split()

count = 0
for i in new_frase:
    for item in i:
        count += 1

print("La frase contiene", count, "caracteres")

# Sin split

frase = input("Escribe una frase: ")
count = 0

for f in frase:
    if f == " ":
        count = count
    else:
        count += 1


print("La frase contiene", count, "caracteres")