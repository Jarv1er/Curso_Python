class Ean:

    def __init__(self, codigo, pares, impares, num_control):
        self.codigo = codigo
        self.pares = pares
        self.impares = impares
        self.num_control = num_control
    
    def validar(self):
        if self.codigo == 8 or self.codigo == 13:
            self.codigo = self.codigo[:-1]
            self.num_control = self.codigo[-1]
        else:
            print("El codigo es incorrecto debe tener 8 o 13 numeros: ")

    def calculo(self):
        for i in self.codigo:
            if i % 2 == 0:
                self.pares += int(self.codigo)
            else:
                self.impares += int(self.codigo)

        if len(self.codigo) == 8:
            self.impares *= 3
        elif  len(self.codigo) == 13:
            self.pares *= 3
        
        self.codigo = self.impares + self.pares
        self.codigo = self.codigo % 10
        self.codigo = 10 - self.codigo
    
    def __str__(self):
        if self.codigo == 10:
            self.codigo = 0
        if self.codigo == self.num_control:        
            return "El codigo es correcto"
        else:
            return "El codigo es incorrecto"


    
        

        
    


       
