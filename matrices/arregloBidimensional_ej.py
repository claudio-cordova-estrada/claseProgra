import numpy as np

matriz = np.array([[0, 1, 2], [3, 4, 5]])
# Los for que tratan con arreglos no toman el valor entero de la lista, sino solo su enumeración
# Por ej. arriba [0, 1, 2] será abajo [0] puesto que se corresponde con la posición 0 de la lista
for f in range (2):
    print([f])
    for c in range (3):
        print(matriz[f][c])

print('-------------------------------------')

lista = [[0, 1, 2], [3, 4, 5]]
matriz2 = np.array(lista)
print(matriz2)

