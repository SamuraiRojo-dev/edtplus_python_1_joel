edad = 17

if edad >= 18: # identacion, espacio que hace referencia a los 4 puntos de espacio
    print("Eres mayor de edad")

else:
    print("Eres menor de edad")

"""
RETO

quiero que le pidas al usuario que le pidas que digite su edad y compares si su edad es mayor o menor de edad.
recuerda validar el tipo de dato y debe haber una variable que indique la mayoria de edad/ EDAD = 18 o 21
"""

mi_edad = input("Cual es tu edad ")
edad = int(mi_edad)
if edad >= (18 or 21):
    print("Eres mayor de edad")
else:
    print("Eres un niño")

print(type(edad))

# Hay dos maneras de hacerlo

edad2 = int(input("Indicame tu edad "))

if edad2 >= (18 or 21):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print(type(edad2))

