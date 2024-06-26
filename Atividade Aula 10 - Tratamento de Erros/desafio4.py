# DESAFIO 04

# Escreva um programa que peça ao usuário para digitar seu nome e idade. 
# Em seguida, exiba uma mensagem personalizada que inclua o nome e a idade. 
# Lide com o erro caso a idade digitada não seja um número.

try:
    exibeTexto = lambda nome,idade: print(f"Seu nome é {nome} e sua idade {idade}")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    exibeTexto(nome, idade)
    
except ValueError:
    print("Favor inserir dados válidos")