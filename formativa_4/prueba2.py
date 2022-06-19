import numpy as np

asiento = np.arange(1, 43).reshape((7, 6))

for i in range(7):
    for c in range(2):
        if c == 0:
            print("|", asiento[i][c], end = " ")
        elif c == 3:
            print("\t", asiento[i][c], end = " ")
        else:
            print("", asiento[i][c], end = " ")
    for c in range(2, 7):
        if c == 0:
            print("|", asiento[i][c], end = " ")
        elif c == 3:
            print("\t", asiento[i][c], end = " ")
        else:
            print("", asiento[i][c], end = " ") #A 
    print("|")
    print("\n")