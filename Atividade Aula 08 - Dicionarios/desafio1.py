# DESAFIO 01

# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. 
# No final mostre o conteúdo da estrutura na tela.

dcAluno = {}
notaCorte = 7.0

dcAluno["nome"] = input("Digite seu nome: ")
dcAluno["media"] = float(input("Entre com sua média: "))

if(dcAluno["media"] >= notaCorte):    
    dcAluno["situacao"] = "Aprovado"
else:    
    dcAluno["situacao"] = "Reprovado"   

for nome, situacao in dcAluno.items():
    print(f"Nome do aluno: {nome} e situação: {situacao}")