def numero():
    return 15

variavelFuncao = numero

print(variavelFuncao() + 5)


def calculaPotencia(valor, expoente=2):
    potencia = valor ** expoente
    print(potencia)
    

valor = int(input("Digite um valor: "))

calculaPotencia(valor)
    