'''
DESAFIO 01
Crie um programa que leia o nome completo de uma pessoas e mostre
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome
'''
# Fabio Jorge Gunji

nomeCompleto = input("Entre com o seu nome completo: ")

print("_____________________________________________________")
# O nome com todas as letras maiúsculas
nomeMaiusculo = nomeCompleto.upper()

# O nome com todas as letras minúsculas
nomeMinusculo = nomeCompleto.lower()

# Quantas letras ao todo (sem considerar espaços)
nomeSemEspaco = nomeCompleto.replace(" ","")
qtdLetras = len(nomeCompleto.replace(" ",""))

# Quantas letras tem o primeiro nome
qtdLetraPrimeiro = nomeCompleto.split()
qtdNome =  len(qtdLetraPrimeiro[0])

print(f"Nome completo: {nomeCompleto}.")
print(f"Nome completo em maiúsculo: {nomeMaiusculo}.")
print(f"Nome completo em minúsculo: {nomeMinusculo}.")
print(f"Quantidade de letras sem espaços: {nomeSemEspaco} - {qtdLetras} letras.")
print(f"Quantidade de letras do primeiro nome: {qtdLetraPrimeiro[0]} - {qtdNome} letras.")
print("_____________________________________________________")