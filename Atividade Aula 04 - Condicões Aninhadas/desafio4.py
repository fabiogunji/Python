#DESAFIO 04

#A confederação Nacional de Natação precisa de uma programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade.

#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 24 anos: SÊNIOR
#Acima: MASTER

from datetime import *

anoNascimento = int(input("Entre com o anos do seu nascimento: "))

mirim = 9
infantil = 14
junior = 19
senior = 25

ano = date.today().year

calculoAno = (ano - anoNascimento)

if (calculoAno <= 9):
    print(f"Mirim! - Ano nascimento: {anoNascimento} e Categoria {calculoAno}")
elif (calculoAno <= 14):
    print(f"Infantil! -  Ano nascimento: {anoNascimento} e Categoria {calculoAno}")
elif (calculoAno <= 19):
    print(f"Junior! -  Ano nascimento: {anoNascimento} e Categoria {calculoAno}")
elif (calculoAno <= 25):
    print(f"Senior! -  Ano nascimento: {anoNascimento} e Categoria {calculoAno}")
else:
    print(f"Master! -  Ano nascimento: {anoNascimento} e Categoria {calculoAno}")
