import random

# Paso 1: Definir las opciones del juego
opciones = ['piedra', 'papel', 'tijera']

# Función para comparar las opciones
def comparar(opcion_usuario, opcion_computadora):
    if (opcion_usuario == 'piedra' and opcion_computadora == 'tijera') or \
       (opcion_usuario == 'papel' and opcion_computadora == 'piedra') or \
       (opcion_usuario == 'tijera' and opcion_computadora == 'papel'):
        return 'Ganaste'
    elif opcion_usuario == opcion_computadora:
        return 'Empate'
    else:
        return 'Perdiste'

# Solicitar al usuario su elección
print("Elige piedra, papel o tijera:")
eleccion_usuario = input().lower()

# Seleccionar una opción aleatoria para el ordenador
opcion_computadora = random.choice(opciones)
# Comparar las opciones y mostrar el resultado
resultado = comparar(eleccion_usuario, opcion_computadora)
print(f"\nComputadora eligió {opcion_computadora}. {resultado}")
