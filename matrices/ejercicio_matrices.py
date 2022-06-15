def coordenadaZ(x, y):
    x = x + 10
    y = y + 15
    return x + y

x = int(input("Ingrese coordenadas del eje X ==> "))
y = int(input("Ingrese coordenadas del eje y ==> "))

for i in range(3):
    z = coordenadaZ(x, y)
    x = x + 1
    y = y + 1
    print(x, '.', y)
    print(z)