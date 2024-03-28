# DESAFIO 03

# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas.

distanciaViagem = float(input("Informe a distância da sua viagem em Km: "))
viagemCurta = 0.5
viagemLonga = 0.45

if distanciaViagem <= 200:
    valorViagem = float(distanciaViagem * viagemCurta)
    print(f"A sua viagem é CURTA de {distanciaViagem} menor que 200 km o valor da viagem será de R$ {valorViagem}")
else: 
    valorViagem = float(distanciaViagem * viagemLonga)
    print(f"A sua viagem é LONGA de {distanciaViagem}, maior que 200 km o valor da viagem será de R$ {valorViagem}")
    

