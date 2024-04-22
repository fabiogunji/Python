try:
    numero = int(input("Digite um valor: "))
except ValueError:
    print("Digite um numero")
else:
    print(numero)