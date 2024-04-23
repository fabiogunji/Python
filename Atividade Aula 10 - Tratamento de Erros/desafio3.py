# DESAFIO 03

# Escreva um programa que solicite ao usuário para digitar um número inteiro e exiba o resultado da sua raiz quadrada. 
# Lide com o erro caso o número seja negativo.
import math

calculaRaiz = lambda n1:math.sqrt(n1) 

try:
    n1 = int(input("Entre com um número inteiro: "))
    print(calculaRaiz(n1))
    
except ValueError:
    print("Favor inserir um número inteiro válido")
