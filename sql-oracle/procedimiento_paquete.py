import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
cursor = connection.cursor()

print("--- PULSA EN LA OPCION ---")
print("1 - Busquda de salario y comision\n"
      "2 - Modificar salario y comision")
opcion = input('Opcion: ')

try:
    if opcion == "1":
        num_emp = input("Número del empleado: ")
        salario = cursor.var(cx_Oracle.NUMBER)
        comision = cursor.var(cx_Oracle.NUMBER)

        args = (salario, comision, num_emp)
        cursor.callproc('emp_salario_comision.search', args)
        print(f"Salario: {salario.getvalue()} \n"
              f"Comision: {comision.getvalue()}")

    elif opcion == "2":
        num_emp = input("Número del empleado: ")
        new_salario = input("Inserta nuevo salario: ")
        new_comision = input("Inserta nueva comision: ")

        args = (new_salario, new_comision, num_emp)
        cursor.callproc('emp_salario_comision.modificar', args)
        print(f"Salario: {new_salario} \n"
              f"Comision: {new_comision}")

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()