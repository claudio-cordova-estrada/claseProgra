import numpy as np

matrizCuadrada = np.identity(3)
print(matrizCuadrada, '\n')

print("Matriz de 4x3")
matriz4x3 = np.arange(1,13).reshape((4, 3))
print(matriz4x3)

print('Usando un ciclo for para imprimir sus elementos')
for elemento in np.nditer(matriz4x3):
    print(elemento, end = ' ')

print('\nArreglo aleatorio de 5 elementos')
arregloAleatorio = np.random.randint(0, 11, 5)
print(arregloAleatorio)