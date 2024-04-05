

from random import randint

escolhaComputador = 0

while True:
    computador = randint(0,10)   
    
    if computador % 2  != 0:
        escolhaComputador = computador
        break
    
print(escolhaComputador)