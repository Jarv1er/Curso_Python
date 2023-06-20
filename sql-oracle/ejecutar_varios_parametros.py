import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
cursor = connection.cursor()

try:
    dp = input("Número de la seguridad social:")
    nombre = cursor.var(cx_Oracle.STRING)
    genero = cursor.var(cx_Oracle.STRING)

    args = (nombre, genero, dp)
    cursor.callproc('devolver_nombre_genero', args)
    print(f"Nombre: {nombre.getvalue()} \n"
          f"Genero: {genero.getvalue()}")


except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()