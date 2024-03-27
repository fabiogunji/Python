#DESAFIO 02
#Crie um programa que leia o nome de uma cidade e siga se ela começa ou não com o nome “Santo”.

nomeCidade = input("Entre com o seu nome de uma cidade: ")

cidade = nomeCidade.split()
primeiroNome = cidade[0]


if "Santo" in primeiroNome:
    print(f"O nome da cidade é {nomeCidade} e começa com Santo")
else:
    print(f"O nome da cidade é {nomeCidade} e NÃO começa com Santo.")
 
