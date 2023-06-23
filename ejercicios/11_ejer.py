# Software tipo línea de comandos que a partir de comandos del usuario 
# muestre el resultado (dicho resultado siempre aparece en la terminal)

# Software que muestra la informacion de un usuario
print("Registre sus datos")
name = input("Escriba su nombre: ")
apellidos = input("Escriba sus apellidos: ")
email = input("Escriba su email: ")

print("Linea de Comandos para mostrar los datos")
print("Escribe el 'nombre de usuario' para mostrar la informacion completa\n\
Escribe 'mostrar apellidos' para mostrar los apellidos\n\
Escribe 'mostrar email' para mostrar el email\n\
Escribe 'quiero hacerme rico ahora' para hacerte rico ahora")

comandos = input()

info = {}
info["Name:"] = name
info["Apellidos:"] = apellidos
info["Email:"] = email

if comandos == name.lower():
    for key, value in info.items():
        print(key, value)

elif comandos == "mostrar apellidos".lower():
    print(info["Apellidos:"])

elif comandos == "mostrar email".lower():
    print(info["Email:"])

elif comandos == "quiero hacerme rico ahora".lower():
    print()
    print("Genial! Una excelente decision!\n Mire su cuenta bancaria y podra ver \
que su dinero ha aumentado en 30.000.000 de Euros.\n Disfrutelo \
y recuerde que lo mas importante es la salud no se lo gaste todo en drogas.")
        
else:
    print("Ha escrito mal el comando, ejecute el programa de nuevo, no voy hacer un 'while'")


