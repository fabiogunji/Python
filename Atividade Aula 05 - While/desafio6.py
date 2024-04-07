# DESAFIO 06

# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar. 

# No final, mostre:
    # A) Qual é o total gasto na compra.
    # B) Quantos produtos custam mais de R$ 100,00.
    # C) Qual é o nome do produto mais barato.
    

vlrMaior100 = qtdProduto = totalGasto = contador = prdMaiort100 =  0
vlrCompra =  vlrMenorPreco = 0.0    
nmProdutoMaisBarato = " "
dictProduto = {}

def validaPreco(produto, preco, vlrMenorPreco):        
    if (preco < vlrMenorPreco): 
        dictProduto.update({produto:preco})       
        
        

while True:    
    produto = (input("Digite o nome do produto: ")).upper()
    preco = float(input("Digite o preço desse produto: "))   
      
    nmProdutoMaisBarato = produto
    qtdProduto += 1        
        
    if preco > 100.0:
        vlrMaior100 += 1  
        vlrCompra += preco  
    else:
        vlrCompra += preco        
               
    validaPreco(produto, preco, vlrMenorPreco)

    continuar = input("Deseja continuar? [S/N]: ").upper()
    
    if continuar == "N":        
        break

        
print(f"#### A) Qual é o total gasto na compra: {vlrCompra:.2f}.")
print(f"#### B) Quantos produtos custam mais de R$ 100,00: {vlrMaior100}.")
print(f"#### C) Qual é o nome do produto mais barato: {nmProdutoMaisBarato}.")
