
dni = int(input("Inserta el numero del dni: "))

result = dni % 23

if result == 6:
    print("Su dni completo es", dni, "Y")
else:
    print("El numero es incorrecto")

print(result)



