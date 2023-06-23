
colores = dict()

colores = {
    "Amarillo": "Yellow",
    "Rosa": "Pink",
    "Azul": "Blue",
    "Blanco": "White",
    "Rojo": "Red"
}

try:
    color = input("Escribe un color: ")
    dato = colores[color]
    print(dato)
except KeyError:
    print("Error: El dato no se encuentra, pueba con otro color")



