# Software que permita sumar y restar (ambas opciones por ejecución) números enteros.

print("Suma y resta dos numeros enteros")

n1 = int(input("Ingresa el primer numero: "))

n2 = int(input("Ingresa el segundo numero: "))

suma = n1 + n2
resta = n1 - n2

print("Suma: {} + {} = {}\nResta: {} - {} = {}".format(n1, n2, suma, n1, n2, resta))