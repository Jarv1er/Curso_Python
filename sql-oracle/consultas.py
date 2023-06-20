import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    salario1 = input("Inserta el primer salario: ")
    salario2 = input("Inserta el segundo salario: ")

    consulta = "SELECT apellido, oficio, salario FROM EMP WHERE SALARIO BETWEEN :s1 AND :s2 "

    cursor.execute(consulta, (salario1, salario2))
    # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable

    for ape, ofi, sal in cursor:
        print("Apellido: ", ape)
        print("Oficio: ", ofi)
        print("Salario: ", str(sal))

except connection.Error as error:
    print("Error: ", error)

connection.close()