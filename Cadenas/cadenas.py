texto = "aprender a programar en python con un simple paso"

lenguaje_de_programacion = "python"

if lenguaje_de_programacion in texto:
    print("si esta la palabra")
else:
    print("no esta la palabra")

# longitud de una cadena
tamano_texto = len(texto)
print(tamano_texto)

#todo mayuscula
texto_mayuscula = texto.upper()
print(texto_mayuscula)

# lower case = todo en minuscula 
texto_minuscula = texto.lower()
print(texto_minuscula)

# title case = todos iniciales en mayuscula
texto_inicial = texto.title()
print(texto_inicial)

# swapcase = pasar todos las palabras a minuscula
texto_inverso = texto.swapcase()
print(texto_inverso)
print(texto_inverso.swapcase())

# count = contar todas las palabras  que hay en el texto que coincidan
conteo_palabras = texto.lower()