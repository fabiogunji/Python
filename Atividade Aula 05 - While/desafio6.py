# DESAFIO 06

# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar. 

# No final, mostre:
    # A) Qual é o total gasto na compra.
    # B) Quantos produtos custam mais de R$ 100,00.
    # C) Qual é o nome do produto mais barato.
    

qtdProduto = totalGasto = 0
vlrMaior100 = 0.0   
prdMaiort100 = 100.0 
vlrCompra = 0.0
lstdMaisBarato = []
prdMaisbarato = " "

def validaPreco(vlr1, vlr2,nome,preco):
    if (vlr1 < vlr2): 
        numeroMenor = vlr1        
    else:             
        numeroMenor = vlr1 
    
    return numeroMenor,nome,preco

while True:    
    produto = (input("Digite o nome do produto: ")).upper()
    preco = float(input("Digite o preço desse produto: "))
    
    continuar = input("Deseja continuar? [S/N]: ").upper()
    
    if continuar == "S":
        qtdProduto += 1        
        
        if preco > prdMaiort100:
            vlrMaior100 += 1  
            vlrCompra += preco  
        else:
            vlrCompra += preco             
        
        lstdMaisBarato.append(validaPreco(preco, preco,produto,preco))
            
        continue
    elif continuar == "N":    
        if preco > prdMaiort100:
            vlrMaior100 += 1  
            vlrCompra += preco 
            
        break
    else:
        print("Favor entrar con S ou N.")
        
print(f"#### A) Qual é o total gasto na compra: {vlrCompra}. ####")
print(f"#### B) Quantos produtos custam mais de R$ 100,00: {vlrMaior100}. ####")
print(f"#### C) Qual é o nome do produto mais barato: {prdMaisbarato}. ####")
