#DESAFIO 03

# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

total = 0

for elemento in range (1,501):      
    if elemento % 2 != 0:        
        if elemento % 3 == 0:         
            total = total + elemento        
else:
    print(f"A soma total dos números impares e multiplos de 3 de 1 a 500 é {total}")
  