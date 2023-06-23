# Software que permita indcar si un número entero es par o impar.

def par_impar(n):
    if n % 2 == 0:
        return f"{n} es par"
    else:
        return f"{n} es impar"
    

n = int(input("Escribe un numero: "))
print(par_impar(n))