#Dada una secuencia de caracteres, obtener dicha secuencia invertida.
def invertir_cadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

# Ejemplo
print(invertir_cadena("hola"))  # Salida: aloh