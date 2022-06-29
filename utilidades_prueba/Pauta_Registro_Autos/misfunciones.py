import os
os.system("cls")

listaPatente = ['AAAA11','BBBB22','CCCC33']
listaMarca = ['MAZDA','FORD','CHEVROLET']
listaAño = [2020,2018,1990]
listaPrecio = [16500000,19500000,2750000]


print("MENU")
print("1. Guardar patente")
print("2. Buscar vehiculo")
print("3. Imprimir lista")
print("4. Salir")

def menu():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion >= 0 and opcion <= 4:
                break
            else:
                print("opcion incorrecta...")
        except:
            print("Error de ingreso")
    return opcion



def ingreso():
    while True:
        patente = input("Ingrese patente: ")
        listaPatente.append(patente)
        if patente != 6:  #Largo de caracteres de la patente
            break
        else:
            print("Patente no valida")

    while True:
        marca = input("Ingrese marca de vehiculo: ").upper()
        listaMarca.append(marca)
        if marca != 2:
            break
        else:
            print("Marca no valida")

    while True:
        año = int(input("Ingrese año de fabricacion: "))
        listaAño.append(año)
        if año > 1900 and año < 2022:
            break
        else:
            print("Año no valido")


    while True:
        precio = int(input("Ingrese precio: "))
        listaPrecio.append(precio)
        if precio > 80000:
            break
        else:
            print("Precio no valido")


def buscar():
    buscar = input("Ingrese patente a buscar: ")
    encontrado = False
    for i in range(len(listaPatente)):
        if buscar == listaPatente[i]:
            encontrado = True
            print(f"Patente : {listaPatente[i]}")
            print(f"Marca   : {listaMarca[i]}")
            print(f"Año     : {listaAño[i]}")
            print(f"Precio  : {listaPrecio[i]}")
            break 
    if encontrado == False:
        input("Patente no ha sido encontrada en la lista")


def imprimir():
    print(" LISTA GENERAL VEHICULOS INSCRITOS")
    print(" =================================")
    print("PATENTE  MARCA        AÑO    PRECIO ")
    print("------------------------------------")
    c = 0
    for i in range(len(listaPatente)):
        print(f"{listaPatente[i]:6s}  {listaMarca[i]:10s} {listaAño[i]:6d}  {listaPrecio[i]:8d}")
        if listaAño[i] < 2011:
            c += 1
    print("------------------------------------")
    print(f"Cantidad total de vehiculos: {len(listaPatente)}")
    print(f"Cantidad de vehiculos con prohibicion de circular: {c}")

