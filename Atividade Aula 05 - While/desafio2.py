# DESAFIO 02

# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999).
contador = 1
parada = 999
soma = 0

while True:
    try:
        jogador = int(input("Entre com um número: "))    
        
        if (type(jogador) == int):
            if jogador == parada:
                print("--------------------------------------------------------------------------------------------------")
                print(f"Parabéns você acertou o código de parada do sistema '{parada}' na {contador}º tentativa.", end=" - ")        
                break
            else:
                print("Tente novamente: ")
                contador += 1
                soma += jogador
                continue 
    except:
        print("Favor entrar con um número inteiro.")
        continue
    
print(f"A soma dos valores digitados foi {soma:.2f}")
print("--------------------------------------------------------------------------------------------------")

    
    