# DESAFIO 04
# Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = float(input("Digite um número: "))

#if numero >= 1 and numero <= 9:
for n in range(0,11):
    print(f"{numero} X {n} = {numero * n:.2f}")
#else:
    #print("Entre com um valor correto")