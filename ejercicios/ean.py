from ValidarEan import Ean

num = input("Introduzca un número EAN (8 o 13 caracteres)")
validar_ean = Ean()
validar_ean.validar(num)
validar_ean.calcular(num)