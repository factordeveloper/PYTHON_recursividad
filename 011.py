#Implementar una función recursiva que permita recorrer una matriz y mostrar sus 
#valores.

def recorrer_matriz(matriz, i=0, j=0):
    if i >= len(matriz):
        return
    if j >= len(matriz[0]):
        recorrer_matriz(matriz, i + 1, 0)
    else:
        print(matriz[i][j], end=" ")
        recorrer_matriz(matriz, i, j + 1)

# Ejemplo
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
recorrer_matriz(matriz)  # Salida: 1 2 3 4 5 6 7 8 9