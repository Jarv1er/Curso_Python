# Software que dada una frase indique su longitud, palabra más larga, letra más usada, 
# letra inicial, letra final y palabra central.

frase = input("Escribe una frase: ") # Input

# Longitud
longitud = len(frase)

# Palabra mas larga
long_palabra = 0
list_frase = frase.split()
for word in list_frase:
    if len(word) > long_palabra:
        long_palabra = len(word)
        longest_word = word

# Letra mas usada
letras = ""

# Letra inicial y final
letra_inicial = frase[0]
letra_final = frase[-1]

# Palabra central
palabra_central = ""

# Output

''' 
longitud: int 
palabra mas larga: string
letra mas usada: string
letra inicial y final: string
palabra central: string
'''

