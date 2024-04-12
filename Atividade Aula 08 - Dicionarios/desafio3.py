# DESAFIO 03

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário 

# se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# Sabendo que ele vai se aposentar após 35 anos de colaboração.

from datetime import date
tempoAposentadoria = 35

dicionario = {
    "nome": input("Digite o nome: "),
    "nascimento": int(input("Entre com o ano de nascimento: ")),
    "carteira": int(input("Inserir o número da carteira de tabalho (0 SE NÃO TIVER): "))
}


idade = date.today().year - dicionario["nascimento"]
del dicionario["nascimento"]
dicionario["idade"] = idade

#print(dicionario)

if dicionario["carteira"] == 0:
    for nome,valor in dicionario.items():
        print(f"Nome do trabalhador: {nome} dados: {valor}")
else:
    anoContratacao = int(input("Insira o ano de contratação: "))
    salario = float(input("Fornaça o salário: "))
    
    tempoTrabalho = tempoAposentadoria - (date.today().year - anoContratacao)
    
    dicionario["contratacao"] = anoContratacao
    dicionario["salario"] = salario
    dicionario["aposentadoria"] = idade + tempoTrabalho

    for nome,valor in dicionario.items():
        print(f">>>> {nome} = {valor}")            