from random import randint

pontuaMaquina = pontuaUsuario = 0

for elemento in range (1,11):
    aleatorio = randint(0,5)
    
    numero = int(input(f"{elemento}º rodada Digiten um número: "))
    
    if aleatorio == numero:
        print("Você acertou!")
        pontuaUsuario += 1
    else:
        print("Você errou!")
        pontuaMaquina += 1
else:
    if pontuaUsuario > pontuaMaquina:
        print(f"Vencedor:  Usuário - {pontuaUsuario} pontos")    
    else:
        print(f"Vencedor:  Máquina - {pontuaMaquina} pontos")
    
    
    