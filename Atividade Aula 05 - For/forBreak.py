from random import randint

maquina = randint(1,20)    

for elemento in range (1,11):   
    
    numero = int(input(f"{elemento}º rodada Digite um número: "))
    
    if numero == maquina:
        print(f">>>> Vencedor:  Usuário. <<<<")  
        print("Fim do game")
        break   
          
else:
    print(f"Vencedor:  Máquina.")    
    print("Fim do game")