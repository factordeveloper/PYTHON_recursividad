#Desarrollar un algoritmo que invierta un numero entero sin convertirlo a cadena

def invertir_numero(n, inverso=0):
    if n == 0:
        return inverso
    else:
        return invertir_numero(n // 10, inverso * 10 + n % 10)

# Ejemplo
print(invertir_numero(1234))  # Salida: 4321