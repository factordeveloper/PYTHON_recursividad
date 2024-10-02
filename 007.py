#Desarrollar un algoritmo que permita convertir un numero entero en sistema 
#decimal a sistema binario.

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Ejemplo
print(decimal_a_binario(10))  # Salida: 1010