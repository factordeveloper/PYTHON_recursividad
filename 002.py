#Implementar una función que calcule la suma de todos los números enteros 
#comprendidos entre cero y un numero entero positivo dado.
def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n - 1)

# Ejemplo
print(suma(5))  # Salida: 15 (0 + 1 + 2 + 3 + 4 + 5)