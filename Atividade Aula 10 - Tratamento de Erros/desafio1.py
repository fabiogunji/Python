# DESAFIO 01

# Escreva um programa que peça ao usuário para digitar dois números e divida o primeiro número pelo segundo. 
# Certifique-se de lidar com a possibilidade de divisão por zero.

def divideNumeros(numero1, numero2):
    return numero1 / numero2

try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite mais um número: "))
except:
    print("Coloque apenas valores numericos.")

print(f"A divisão de {n1} e {n2} é igual a {divideNumeros(n1,n2)}")