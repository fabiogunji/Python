#DESAFIO 06

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

razao = int(input("Informe a razao da progressao aritimetica: "))
qtdTermo = int(input("Informe a de termos da progressao aritimetica: "))
inicioPa = int(input("Informe o número inicial da progressao aritimetica: "))
lstPa = []
contador = 1

for n in range (inicioPa,qtdTermo,razao):    
    if n == inicioPa:
        primeiroTermo = n      
    
    if contador <= 10:
        lstPa.append(n)
        
    contador += 1
else:
    print(f"Primerio termo da PA: {primeiroTermo}")
    print(f"Lista dos primeiros 10 termos da PA: {lstPa}")
    