# DESAFIO 06

# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar. 

# No final, mostre:
    # A) Qual é o total gasto na compra.
    # B) Quantos produtos custam mais de R$ 100,00.
    # C) Qual é o nome do produto mais barato.
    

vlrMaior100 = qtdProduto = contador = 0
vlrCompra =  vlwProdutoMaisBarato = 0.0  
prdMaiort100 = 100.0  
nmProdutoMaisBarato = " "               

while True:    
    produto = (input("Digite o nome do produto: ")).upper()    
    preco = float(input("Digite o preço desse produto: "))   
      
    qtdProduto += 1     
    contador += 1   
        
    if preco > prdMaiort100:
        vlrMaior100 += 1  
        vlrCompra += preco  
    else:
        vlrCompra += preco        
    
    if contador == 1:
        nmProdutoMaisBarato = produto
        vlwProdutoMaisBarato = preco
    elif preco < vlwProdutoMaisBarato:        
        nmProdutoMaisBarato = produto
        vlwProdutoMaisBarato = preco      
    
    continuar = input("Deseja continuar? [S/N]: ").upper()
    
    if continuar == "N":        
        break

        
print(f"#### A) Qual é o total gasto na compra: R$ {vlrCompra:.2f}.")
print(f"#### B) Quantos produtos custam mais de R$ 100,00: {vlrMaior100}.")
print(f"#### C) Qual é o nome do produto mais barato: {nmProdutoMaisBarato} com o valor de R$ {vlwProdutoMaisBarato:.2F}.")
