#DESAFIO 03
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nomeCompleto = input("Entre com o seu nome completo: ")

if "SILVA" in nomeCompleto.upper():
    print(f"O nome é {nomeCompleto} e contém Silva.")
else:
    print(f"O nome é {nomeCompleto} e NÃO contém Silva.")
