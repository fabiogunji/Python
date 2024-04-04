# DESAFIO 06
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

razao = int(input("Informe a razao da progressao aritimetica: "))
inicioPa = int(input("Informe o número inicial da progressao aritimetica: "))

qtdTermo = int(input("Informe a de termos da progressao aritimetica: "))
# como calcular o último termo (10)
#qtdTermo = (inicioPa + (10 - 1 ) * razao) + razao

# print("Fabio", end="-")
# print("Gunji")
# resultado = Fabio-Gunji

lstPa = []
contador = 1

for n in range (inicioPa,qtdTermo,razao):    
    if n == inicioPa:
        primeiroTermo = n      
    
    if contador <= 10:
        lstPa.append(n)
        
    contador += 1
else:
    print(f"Primerio termo da PA: {primeiroTermo} ", end=" -----> ")
    print(f"Lista dos primeiros 10 termos da PA: {lstPa}")
    