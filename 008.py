#Desarrollar un algoritmo que cuente la cantidad de dígitos de un numero entero.

def contar_digitos(n):
    if n == 0:
        return 0
    else:
        return 1 + contar_digitos(n // 10)

# Ejemplo
print(contar_digitos(12345))  # Salida: 5