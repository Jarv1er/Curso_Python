class Dni:
    calculo = 0
    letra = ""
    def __init__(self):
        self.letra = "TRWAGMYFPDXBNJZSQVHLCKET"

    def calcular_dni(self, numero):
        self.calculo = numero % 23
        self.letra = self.letra[self.calculo]
    
    def __str__(self):
        return "La letra de su Dni es: " + self.letra
    

        