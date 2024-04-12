# DESAFIO 01

# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. 
# No final mostre o conteúdo da estrutura na tela.

dcAluno = {}
notaCorte = 7.0

nome = input("Digite seu nome: ")
media = float(input("Entre com sua média: "))

if(media >= notaCorte):
    dcAluno["Nome"] = nome
    dcAluno["Media"] = media
    dcAluno["Situacao"] = "Aprovado"
else:
    dcAluno["Nome"] = nome
    dcAluno["Media"] = media
    dcAluno["Situacao"] = "Reprovado"
   

print(dcAluno)