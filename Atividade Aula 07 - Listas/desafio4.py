# DESAFIO 04

# Crie um programa que vai ler vários números e colocar em uma lista.

# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.

lstValores = []
lstValoresPares = []
lstValoresImpares = []

contador = 0

while True:    
    lstValores.append(int(input(f"Entre com o {contador}º número inteiro: ")))
    contador += 1
    
    if input("Deseja continuar? [S/N]: ").upper() == "S":
        continue
    else:
        break
    
for i in lstValores:
    if i % 2 == 0:
        lstValoresPares.append(i)
    else:
        lstValoresImpares.append(i)
        
    
print(f"A lista original é {lstValores} e a lista de números pares é {lstValoresPares} e a lista de números ímpares é {lstValoresImpares}") 
        
    