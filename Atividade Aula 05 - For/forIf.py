from random import randint

aleatorio = randint(0,5)
pontuaMaquina = 0
pontuaUsuario = 0

for elemento in range (1,11):
    numero = int(input(f"{elemento}º rodada Digiten um número: "))
    
    if aleatorio == numero:
        print("Você acertou!")
        pontuaUsuario = pontuaUsuario + 1
    else:
        print("Você errou!")
        pontuaMaquina = pontuaMaquina + 1
    
    
    