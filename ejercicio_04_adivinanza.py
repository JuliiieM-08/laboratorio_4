"""
EJERCICIO 04: Adivina el número

1. Selecciona un número entero y almacenalo en una variable. 
2. Pide al usuario que lo adivine dentro de un bucle while. 
3. En cada intento, el programa debe indicar si el número buscado es mayor o menor que el ingresado, hasta que lo adivine.
"""
import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("--- ¡Juego: Adivina el Número! ---")
print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")

# 2. Bucle while para pedir al usuario que lo adivine
adivinado = False

while not adivinado:
    try:
        intento = int(input("\nIngresa tu número: "))
        intentos += 1

        # 3. Indicar si el número buscado es mayor, menor o si acertó
        if intento < numero_secreto:
            print("El número buscado es MAYOR.")
        elif intento > numero_secreto:
            print("El número buscado es MENOR.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intento(s).")
            adivinado = True  # Termina el bucle

    except ValueError:
        print("Entrada no válida. Ingrese únicamente números enteros.")
