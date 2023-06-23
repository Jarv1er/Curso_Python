import sys

def controlErrores():
    try:
        dividendo = int(input("Inserta dividendo: "))
        divisor = int(input("Insertar divisor: "))
        resultado = dividendo / divisor
        print(f"Resultado division: {resultado}")
    except ValueError:
        print("Error, debes introducir numero")
    except ZeroDivisionError:
        print("¡¡¡Error!!!. El divisor no puede ser cero")
    except:
        print(f"Error: {sys.exc_info()}")
    finally:
        print("Entra")

controlErrores()

