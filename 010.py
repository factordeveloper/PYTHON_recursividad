#Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) 
#de dos números enteros.

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

# Ejemplo
print(mcd(48, 18))  # Salida: 6