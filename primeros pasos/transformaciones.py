# Concatenaciones o Union entre cadenas de texto (str)

nombre = "Joel"
print(type(nombre))

apellido = "Delpino"
print("Este es la union del texto sin espacio entre el nombre y el apellido:", nombre + apellido)
print("Este es la union del texto sin espacio entre el nombre y el apellido:", nombre + " " + apellido)

# Reto
valor1 = 20
valor2 = 20

valor3 = "20"
valor4 = "20"

print(valor1 + valor2)
print(valor3 + valor4)

print("Valor es de tipo ->", type(valor1))
print("Valor es de tipo ->", type(valor2))
print("Valor es de tipo ->", type(valor3))
print("Valor es de tipo ->", type(valor4))

print("Para hacer la operacion entre cadena de texto que sean numeros: ", int(valor3) + int(valor4))

""""
Reto 
1.- Quiero que le pregunten al usuario su nombre  y apellido
2.- Quiero que unan dos cadenas de texto y un numero entero (Ejemplo: nombre, apellido y edad.)
3.- Quiero que realicen una suma y una resta entre una cadena de texto y un numero entero

"""

mi_nombre = input("Cual es tu nombre ")
print(mi_nombre)

mi_apellido = input("Cual es tu apellido ")
print(mi_apellido)

nombre = "Joel"
apellido = "Delpino"
edad = "11"
print(nombre + " " + apellido + " " + edad)


