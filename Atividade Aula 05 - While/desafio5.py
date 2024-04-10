# DESAFIO 05

# Crie um programa que leia a idade e o sexo de varias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 

# No final, mostre:
    # A) Quantas pessoas tem mais de 18 anos.
    # B) Quantos homens foram cadastrados.
    # C) Quantas mulheres tem menos de 20 anos.

qtdPessoas = qtdMaior18 = qtdHomens = qtdMulherMenor20 = 0    

while True:    
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite o seu sexo: [M/F]: ").upper()
    
    continuar = input("Deseja continuar? [S/N]: ").upper()
    
    if continuar == "S":
        qtdPessoas += 1        
        
        if sexo == "M":
            qtdHomens += 1            
            if idade > 18:
                qtdMaior18 += 1
        else:
            if idade > 18:
                qtdMaior18 += 1
            
            if idade < 20:
                qtdMulherMenor20 += 1
            
            
        continue
    elif continuar == "N":    
        if idade > 18:
            qtdMaior18 += 1
        
        if sexo == "M":
            qtdHomens += 1                    
        else:
            if idade > 18:
                qtdMaior18 += 1
            
            if idade < 20:
                qtdMulherMenor20 += 1   
            
        break
    else:
        print("Favor entrar con S ou N.")
        
print(f"#### A) Quantas pessoas tem mais de 18 anos: {qtdMaior18}.")
print(f"#### B) Quantos homens foram cadastrados: {qtdHomens}.")
print(f"#### C) Quantas mulheres tem menos de 20 anos: {qtdMulherMenor20}.")

