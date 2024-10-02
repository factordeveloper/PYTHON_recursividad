#Desarrollar el algoritmo de Euclides para calcular también el mínimo común 
#múltiplo (MCM) de dos números enteros.


def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

# Ejemplo
print(mcd(48, 18))  # Salida: 6

#############################################
def mcm(a, b):
    return abs(a * b) // mcd(a, b)

# Ejemplo
print(mcm(48, 18))  # Salida: 144