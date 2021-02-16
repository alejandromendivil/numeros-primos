# Capturar un número y decir si es un numero primo o no
# Ejemplo: 88 No es un número primo
# Ejemplo: 11 Si es un número primo

num = int(input("Ingrese un número:"))


def validarNumero (num):
    
    if num < 2:
        return False

    for i in range (2, num):
        if num % i == 0:
            return False

        if num % i != 0:
            return True

if validarNumero(num) == True:
    print (num,"Si es un número primo")

if validarNumero(num) == False:
    print (num,"No es un número primo")
    
