# Software que permita refistrarse a un usuario 
# con nombre, apellidos, dni, dirección, email y contraseña.

print("Registrese como usuario")

# Input y variables
name = input("Escriba su nombre: ")
apellidos = input("Escriba sus apellidos: ")
dni = input("Escriba su dni: ")
email = input("Escriba su email: ")
password = input("Escriba su contraseña: ")

# Output
print("Informacion de usuario")

print(f"Nombre: {name.title()}\nApellido: {apellidos.title()}\nDni: {dni.title()}\
        \nEmail: {email}\nContraseña: {password}")
