#DESAFIO 05

#Faça um programa que leia o nome completo de uma pessoa,mostrando em seguida o primeiro e o ultimo nome separadamente
#Exemplo: Ana Maria De Souza
#Primeiro: Ana
#Ultimo: Souza


nomeCompleto = input("Entre com o seu nome completo: ")

primeiroNome = nomeCompleto.split()

ultimoNome = nomeCompleto.split()

print(f"O nome completo digitado é {nomeCompleto}, o primeiro é {primeiroNome[0]} e o último nome é {ultimoNome[-1]}.")