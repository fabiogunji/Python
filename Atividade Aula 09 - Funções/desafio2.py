# DESAFIO 02

# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# Ex:
# escreva(‘Olá, mundo!!’)
# Saída
# -----------------------------------
# Olá, mundo
# -----------------------------------

def escreva(texto):    
    print("-" * len(texto))
    print(texto)
    print("-" * len(texto))
        
escreva("Tinha que ser o Chaves")