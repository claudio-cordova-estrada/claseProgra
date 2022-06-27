# Función de pruebas
def validaInt (p_valor):
    try:
        pass
    except:
        p_valor = int(input("Valor ingresado incorrecto, intentelo nuevamente"))

# Campo de pruebas
a = int(input("==> "))
validaInt(a)
print("a")