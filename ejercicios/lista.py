

print("--------------LISTAS-------------")

print("CREANDO LISTAS DE ENTEROS")
edades = [20,84,18,41,36,25]

print("Edad 1:",edades[0])
print("Edad 2:",edades[1])

print("CREANDO LISTAS DE CADENAS")
nombre = ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]

print("Nombre 4:",nombre[3])
print("Nombre 3:",nombre[2])

print("CREANDO LISTAS DE CADENAS")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]

nombre.insert(1, "Pepito")
print(nombre) #Mostramos la cadena con todos los valores de la lista
print("Nombre 3:",nombre[2])

print("CREANDO LISTAS DE CADENAS")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]

nombre.remove("Sara")
print(nombre) #Mostramos la cadena con todos los valores de la lista

print("CREANDO LISTAS DE CADENAS")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]

del nombre[1:]
print(nombre) 

print("CREANDO LISTAS DE CADENAS")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]

del nombre[:]
print(nombre)

print("CREANDO LISTAS DE CADENAS")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]
numeroelementos=len(nombre)
print("Número de elementos:",numeroelementos)

print("CREANDO LISTAS DE CADENAS")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]

print("Andrea" in nombre) #Preguntamos si el elemento Andrea existe en la lista

print("Pepito" in nombre) #Preguntamos si el elemento Pepito existe en la lista

print("ORDENANDO LISTAS ASCENDENTE")
notas= [1,10,6,7,4,9]
notas.sort()
print("Nota más baja:",notas[0])
print("Segunda nota más baja:",notas[1])

print("ORDENANDO LISTAS DESCENDENTE")
notas.sort(reverse=True)

print("Nota más alta:",notas[0])
print("Segunda nota más alta:",notas[1])

print("--------------LISTAS-------------")

print("ORDENANDO LISTAS ASCENDENTE")
alumnos= ["BENITO","FLORO","ALEX","ANDREA","ZAMORA"]
alumnos.sort()
print("Primer alumno de la lista:",alumnos[0])
print("Segundo alumno de la lista:",alumnos[1])


print("ORDENANDO LISTAS DESCENDENTE")
alumnos.sort(reverse=True)

print("Último alumno de la lista:",alumnos[0])
print("Penúltimo alumno más alta:",alumnos[1])

