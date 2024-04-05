# DESAFIO 03

# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

contador = soma = numeroMaior = numeroMenor = 0
media = 0.0

def validaMaior(numero1, numero2):
    if (numero1 > numero2): 
        numeroMaior = numero1        
    else:             
        numeroMaior = numero2
    return numeroMaior
        
                
def validaMenor(numero1, numero2):
    if (numero1 < numero2): 
        numeroMenor = numero1        
    else:             
        numeroMenor = numero2 
    
    return numeroMenor

def calculaMedia(soma, contador):
    return soma/contador
    
while True:
    try: 
        jogador = int(input("Entre com um número inteiro: "))   
        
        contador += 1
          
        if (type(jogador) == int): 
            soma += jogador           
            if contador == 1:                
                numeroMaior = jogador
                numeroMenor = jogador
            else:
                numeroMaior = validaMaior(jogador, numeroMaior)
                numeroMenor = validaMenor(jogador, numeroMenor)                    
            
        continuar = input("Deseja continuar? [S/N]: ").upper()
        
        if continuar == "S":
            continue
        elif continuar == "N":
            media = calculaMedia(soma,contador)
            break
        else:
            print("Favor entrar con S ou N.")        
        
    except:
        print("Favor entrar con um número inteiro.")
        continue


print(f"A média entre todos os valores é: {media:.2f}")
print(f"Numero maior digitado foi: {numeroMaior}")
print(f"Numero menor digitado foi: {numeroMenor}")





