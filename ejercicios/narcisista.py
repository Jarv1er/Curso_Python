
numero = input("Insertra un numero: ")
narci = 0
long_num = len(numero)

for n in range(long_num):
    narci += pow(int(numero[n]), long_num)

if narci == int(numero):
    print("El numero es narcisista")
else:
    print("El numero no es narcisista")