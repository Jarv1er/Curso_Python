

def control_errores():
    try:
        numero = int(input("Inserta un numero: "))
        print("Numero: ", numero)
    except ValueError:
        print("Error debes introducir un numero")
        control_errores()
        
control_errores()