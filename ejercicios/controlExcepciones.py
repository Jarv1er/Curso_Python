
premios = [166116.06, 133948.48, 32353.38, 1528.22, 123.13, 66.37, 44.89, 15.91]

numero = int(input("Inserte el numero del premio a mostrar: "))

try:
    print(f"Premio obtenido:", premios[numero-1])
except IndexError:
    print("Error!!!: El indice del premio no se encuentra en la lista")

