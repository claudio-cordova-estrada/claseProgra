import numpy as np
arregloA = np.arange(21)

yourMom = arregloA.max()
yourMom2 = (np.where(arregloA == yourMom))
print (yourMom2[0])