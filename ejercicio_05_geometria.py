"""
EJERCICIO 05: Menú de cómputo geométrico.

Complete las funciones para que al ejecutar el programa, se muestre el menú y se le pida al usuario ingresar una de las opciones
(1 - 4). 
    - Si escoge 1, se pide ingresar el valor del radio, se calcula el radio y se muestra en pantalla
    - Si se escoge 2, se pide ingresar el valor de la base y la altura, se calcula el area del rectángulo y se muestra en pantalla
    - Si se escoge 3, se pide ingresar el valor de la base y la altura, se calcula el perímetro del rectángulo y se muestra en pantalla
    - Si se escoge 4, se sale del menú y termina el programa
    - Si se ingresa cualquier otra opcion, se imprime "Opción inválida. Intente de nuevo."

"""


def area_circulo(radio):
    # Calcular el área (π * r^2) y mostrar resultado
    area = math.pi * (radio ** 2)
    print(f"El área del círculo con radio {radio} es: {area:.2f}\n")

def area_triangulo(base, altura): 
    # Calcular el área ((base * altura) / 2) y mostrar resultado
    area = (base * altura) / 2
    print(f"El área del triángulo con base {base} y altura {altura} es: {area:.2f}\n")

def perimetro_rectangulo(base, altura):
    # Calcular el perímetro (2 * (base + altura)) y mostrar resultado
    perimetro = 2 * (base + altura)
    print(f"El perímetro del rectángulo con base {base} y altura {altura} es: {perimetro}\n")

def menu():
    activo = True
    while activo:
        print("--- CALCULADORA GEOMÉTRICA ---")
        print("1. Área de un Círculo")
        print("2. Área de un Triángulo")
        print("3. Perímetro de un Rectángulo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        match opcion:
            case "1":
                try:
                    x = float(input("Ingrese el radio del círculo: "))
                    area_circulo(x)
                except ValueError:
                    print("Por favor, ingrese un número válido.\n")
            case "2":
                try:
                    x = float(input("Ingrese la base del triángulo: "))
                    y = float(input("Ingrese la altura del triángulo: "))
                    area_triangulo(x, y)
                except ValueError:
                    print("Por favor, ingrese números válidos.\n")
            case "3":
                try:
                    x = float(input("Ingrese la base del rectángulo: "))
                    y = float(input("Ingrese la altura del rectángulo: "))
                    perimetro_rectangulo(x, y)
                except ValueError:
                    print("Por favor, ingrese números válidos.\n")
            case "4":
                print("Saliendo de la calculadora...")
                activo = False
            case _:
                print("Opción inválida. Intente de nuevo.\n")

# Ejecutar el menú interactivo
