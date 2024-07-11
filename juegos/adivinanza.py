import random

print("¡Bienvenido al juego de 'Adivina el número'!")
print("La PC pensó en un número del 1 al 35. ¿Puedes adivinarlo?🤔🤔")

aleatorio = random.randrange(1, 35)
error = 0

while error < 7:
    adivinar = int(input("Introduce tu numero para adivinar: "))
    error += 1

    if adivinar == aleatorio:
        print("¡Felicitaciones, has asertado el número que la PC penso😁👍!")
        break
    elif adivinar < aleatorio:
        print("El número es mayor ☝️")
    else:
        print("El número es menor 👇")

if error == 7:
    print("Lo siento, no lo lograste el número era", aleatorio,"😒😒👎")
