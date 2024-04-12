# DESAFIO 05

# Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Um listagem com as pessoas mais leves

lstNomePeso = []
tpPessoas = ()
contador = 1

while True:    
    nome = input(f"Entre com o {contador}º nome: ").upper()
    peso = int(input(f"Entre com o {contador}º peso: "))
    
    tpNomePeso = (nome,peso)
    lstNomePeso.append(tpNomePeso)
    
    contador += 1
  
    if input("Deseja continuar? [S/N]: ").upper() == "S":
        continue
    else:
        break
    
tpPessoas = tuple(lstNomePeso)
   

# print(len(lstNomePeso))

print(f"A) Quantas pessoas foram cadastradas é {len(lstNomePeso)}.")
print(f"B) Uma listagem com as pessoas mais pesadas {sorted(tpPessoas)}")
print(f"C) Um listagem com as pessoas mais leves")

