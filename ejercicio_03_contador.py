"""
EJERCICIO 03: Contador de vocales

Dada una frase escrita por el usuario, recorre cada letra e indica la cantidad de vocales (a, e, i, o, u) que tiene la palabra.
"""
frase = input("Ingrese una frase: ")
palabras = frase.split()

# Definir el conjunto de vocales (incluye mayúsculas y tildes)
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

print("\n--- Conteo de vocales por palabra ---")

for palabra in palabras:
    contador_palabra = 0
    
    # Recorrer cada letra de la palabra actual
    for letra in palabra:
        if letra in vocales:
            contador_palabra += 1
            
    
    print(f"La palabra '{palabra}' tiene {contador_palabra} vocal(es).")