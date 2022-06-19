"""Crear un arreglo unidimensional con nombre arregloA y de tamaño 100, con elementos aleatorios de números enteros del 0 al 500, luego:
Mostrar por pantalla sólo los valores que se encuentren en los índices pares del arreglo.
Mostrar el elemento mayor del arreglo.
Mostrar el índice (posición) del elemento mayor.
Mostrar el elemento menor del arreglo.
Generar la copia de arreglo A y multiplicar por 3 cada elemento. Mostrar resultado.
Mostrar la suma de los elementos del segundo arreglo.
Calcular el promedio de los elementos del segundo arreglo."""

import numpy as np

arregloA = np.arange(11)
arregloA = np.append(arregloA, 3)

print(arregloA)
print(arregloA[::2])

print(np.argmax(arregloA))
print (np.where(arregloA == arregloA.max())[0])

print(np.argmin(arregloA))

arregloB = arregloA * 3
print(arregloB)

print(np.sum(arregloB))

print(np.average(arregloB))