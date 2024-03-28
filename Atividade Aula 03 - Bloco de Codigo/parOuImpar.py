
numero = int(input("Digite um valor: "))

def valida_par(numero, resto):
    if resto == 0:
        print(f"O valor {numero} é par")
    else:
        print(f"O valor {numero} é impar")

resto = numero % 2

valida_par(numero, resto)


    