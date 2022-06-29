def recorredor1Lista (p_algo):
    if not p_algo:
        print("Su lista se encuentra vacía, intentelo nuevamente")
    else:
        for i in lista:
            print(i, end=" ")
        print()

lista = []

while True:
    algo = int(input("""Por favor ingrese la opción que desee:
1.- asfg
2.- asdf

==> """))
    if algo == 1:
        a = input("Primera cosa ==> ")
        b = input("Segunda cosa ==> ")
        c = input("Tercera cosa ==> ")

        jaj = [a, b, c]
        lista.append(jaj)
    elif algo == 2:
        recorredor1Lista(lista)