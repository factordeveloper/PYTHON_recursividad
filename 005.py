#Desarrollar una función que permita convertir un numero romano en un numero 
#decimal.

def romano_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(romano) == 1:
        return valores[romano]
    else:
        if valores[romano[0]] >= valores[romano[1]]:
            return valores[romano[0]] + romano_a_decimal(romano[1:])
        else:
            return romano_a_decimal(romano[1:]) - valores[romano[0]]

# Ejemplo
print(romano_a_decimal("IX"))  # Salida: 9