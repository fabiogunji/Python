# DESAFIO 05

# Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Um listagem com as pessoas mais leves

from operator import itemgetter

lstNomePeso = []
contador = 1

while True:    
    nome = input(f"Entre com o {contador}º nome: ").upper()
    peso = int(input(f"Entre com o {contador}º peso: "))
    
    tpNomePeso = (nome,peso)
    lstNomePeso.append(tpNomePeso)
    
    contador += 1
  
    if input("Deseja continuar? [S/N]: ").upper() == "N":
        break
 
print(f"A) Quantas pessoas foram cadastradas: {len(lstNomePeso)}.")
print(f"B) Uma listagem com as pessoas mais pesadas: {sorted(dict(lstNomePeso).items(), key=itemgetter(1),reverse=True)}")
print(f"C) Um listagem com as pessoas mais leves: {sorted(dict(lstNomePeso).items(), key=itemgetter(1))}")

