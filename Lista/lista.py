# Listas en python []
numero = [1, 2, 3, 4, 5]
print(type(numero))

# Lista de str o cadena de texto
tareas = ["Aprender python", "Resolver retos", "Resolver problemas"]
print(tareas)

# Lista de diferentes tipos de datos
diferentes_tipos_datos = [1, "cadena de texto", True, False]
print(diferentes_tipos_datos)

# Indice de cada arreglo
print("Mostrando el indice [0] del elemento del arreglo numero ->", numero[0])
print("Mostrando el indice [1] del arreglo tareas ->", tareas[1])
print("Mostrando el indice [3] del arreglo del elemento diferentes_tipos_datos -> ", diferentes_tipos_datos[3])

# Mutacion = Modificar el arreglo original
tareas[1] = "Ya he resuelto el reto 1"
tareas[2] = "ya he resuelto el reto 2"
print("Lista modificada ->", tareas)

# Slicing o recorte o pedazo
print(numero[:3])
print(numero[2:])
print(numero[1:3])

# Operador in = en = booleano
print(True in diferentes_tipos_datos)
print("cadena de texto" in diferentes_tipos_datos)
print("Otra cosa que no este" in diferentes_tipos_datos)
