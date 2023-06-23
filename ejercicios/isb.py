
isbn = input("Inserta un numero: ")
suma = 0

if len(isbn) == 10:
    for n in range(0, 10):
        suma += (int(isbn[n] * (n + 1)))
    if suma % 11 == 0:
        print("El numero Isbn es correcto")
    else:
        print("El numero Isbn es incorrecto")
else:
    print("El numero Isbn debe tener 10 numeros")

