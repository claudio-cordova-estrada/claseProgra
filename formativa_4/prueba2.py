"""import numpy as np

asiento = np.arange(1, 43).reshape((7, 6))

for i in range(7):
    for c in range(6):
        if c == 0:
            print("|", asiento[i][c], end = " ")
        elif c == 3:
            print("\t", asiento[i][c], end = " ")
        else:
            print("", asiento[i][c], end = " ")
    print("|")
    print("\n")"""

usuario = [[20123, [1, 4, 6, 3, 2], "blabla", "xd"]] 
listaPasajeCompra = []

compra = 1

while compra:
    compra = int(input("Ingrese hasta marcar 0: "))
    if compra != 0:
        listaPasajeCompra.append(compra)
        for i in listaPasajeCompra:
            for c in usuario:
                if c[1] == i:
                    print()