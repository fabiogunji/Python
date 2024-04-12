# DESAFIO 01

# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. 
# No final mostre o conteúdo da estrutura na tela.

dcAluno = {}
notaCorte = 7.0

dcAluno["nome"] = input("Digite seu nome: ")
dcAluno["media"] = float(input("Entre com sua média: "))

if(dcAluno["media"] >= notaCorte):    
    dcAluno["Situacao"] = "Aprovado"
else:    
    dcAluno["Situacao"] = "Reprovado"   

print(dcAluno)