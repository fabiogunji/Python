#DESAFIO 03

#Crie um programa que leia duas notas entre 0 a 10 de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.

#Média abaixo de 5.0: REPROVADO

#Média entre 5.0 a 6.9: RECUPERAÇÃO

#Média igual ou superior a 7.0: APROVADO

nota1 = float(input("Entre com a primeira nota entre 0 a 10: "))
nota2 = float(input("Entre com a segunda nota entre 0 a 10: "))

if ((nota1 > 10) or (nota1 < 0) and (nota2 > 10) or (nota2 < 0)):    
    print(f"Insira valores entre 0 e 10 - Nota 1: {nota1} e Nota 2: {nota2}")
else:
    mediaNota = ((nota1 + nota2) / 2)

    if(mediaNota >= 7.0):
        print(f"Aluno aprovado! - Nota 1: {nota1}, Nota 2: {nota2} e e sua média: {mediaNota}")
    elif ((mediaNota >= 5.0) and (mediaNota <= 6.9)):
        print(f"Aluno em recuperação! - Nota 1: {nota1}, Nota 2: {nota2} e e sua média: {mediaNota}")
    elif (mediaNota <= 5.0):
        print(f"Aluno em reprovado! - Nota 1: {nota1}, Nota 2: {nota2} e e sua média: {mediaNota}")

    