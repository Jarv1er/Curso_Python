
semana = ("sabado", "domingo", "lunes", "martes", "miercoles", "jueves", "viernes" )

dia = int(input("Inserta el dia: "))
mes = int(input("Inserta el mes: "))
year = int(input("Inserta el year: "))

op1 = ((mes + 1) * 3) // 5
op2 = year // mes
op3 = year // 100
op4 = year // 400

op5 = dia + (mes * 2) + year + op1 + op2 - op3 + op4 + 2
op6 = op5 // 7
op7 = op5 - (op6 * 7)
dia_semana = semana[op7]

print(dia_semana)




