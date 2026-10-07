"""
EJERCICIO 01: Tabla de multiplicar

1. Pide al usuario ingresar un número
2. Garantice la entrada correcta
3. Imprime la tabla de multiplicar del 1 al 10 del número ingresado. Utilice un bucle for
"""
try: 
    número = int (input("ingrese un número entero"))
    for i in range (1, 11):
       print(número*i)

except ValueError:
    print ("Entrada invalida. Ingrese por favor un número entero")

    

