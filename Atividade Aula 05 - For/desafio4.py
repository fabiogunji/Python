#DESAFIO 04

#Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input("Digite um número entre 1 e 9: "))

if numero >= 1 and numero <= 9:
    for n in range(1,11):
        print(f"{numero} X {n} = {numero * n}")
else:
    print("Entre com um valor correto")