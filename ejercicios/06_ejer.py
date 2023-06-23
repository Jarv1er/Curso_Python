# Software que permita validar a un usuario con su contraseña, ofreciéndole N intentos 
# (N es un número entre 1 y 5 y se le asigna a cada usuario aleatoriamente). 
# Si falla sus intentos, debe esperar entre 5 y 20 minutos (también se decide de forma aleatoria)

import random

password = input("Escriba su contraseña: ")
confirmacion = input("Confirme la contraseña: ")

intentos = random.randrange(1, 5)
fallo = random.randrange(5, 20)

if password != confirmacion:
#   intentos = 1
    while intentos < 6:
        print("La contraseña es incorrecta")
        password = input("Escriba su contraseña: ")
        confirmacion = input("Confirme la contraseña: ")
        intentos += 1
        if intentos > 4:
            break
    print(f"Ha cosumido demasiados intentos debe esperar {fallo} minutos")
    
else:
    print("La contraseña es correcta puede pasar")          

