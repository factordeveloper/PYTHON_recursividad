#1. Implementar una función que permita obtener el valor en la sucesión de Fibonacci 
#para un numero dado.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo
print(fibonacci(5))  # Salida: 5