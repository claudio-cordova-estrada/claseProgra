import numpy as np

asiento = np.arange(1, 43).reshape((7, 6))

"""reserva = int(input("-->"))

for a in range(7):
    for x in range(6):
       if asiento[a][x] == reserva:
           asiento[a][x] = 0
           """
           
for a in range(7):
    for x in range(6):
        if x == 0:
            print("|", asiento[a][x], end=" ")
        elif x == 3:
            print("\t", asiento[a][x], end=" ")
        else:
            print("",asiento[a][x], end=" ")
    print("|")
    print("\n")