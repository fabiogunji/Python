# DESAFIO 04

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

try:
    numero1 = int(input("Entre com um número inteiro: "))
    numero2 = int(input("Entre com um número inteiro: "))
    numero3 = int(input("Entre com um número inteiro: "))


    def validaMaior(numero1, numero2, numero3):
        if numero1 > numero2:
            if numero1 > numero3:
                print(f"maior {numero1}")
            else:        
                if numero3 > numero2:                    
                    print(f"Para os números inseridos {numero1}, {numero2} e {numero3} o maior é {numero3}")
        else:
            if numero2 > numero3:
                print(f"Para os números inseridos {numero1}, {numero2} e {numero3} o maior é {numero2}")                
            else:                
                print(f"Para os números inseridos {numero1}, {numero2} e {numero3} o maior é {numero3}")                
                
    def validaMenor(numero1, numero2, numero3):
        if numero1 < numero2:
            if numero1 < numero3:                
                print(f"Para os números inseridos {numero1}, {numero2} e {numero3} o menor é {numero1}")                
            else:        
                if numero3 < numero2:                    
                    print(f"Para os números inseridos {numero1}, {numero2} e {numero3} o menor é {numero3}")                    
        else:
            if numero2 < numero3:                
                print(f"Para os números inseridos {numero1}, {numero2} e {numero3} o menor é {numero2}")                
            else:                
                print(f"Para os números inseridos {numero1}, {numero2} e {numero3} o menor é {numero3}")                

    validaMaior(numero1, numero2, numero3)
    validaMenor(numero1, numero2, numero3)
except:
    print("Entre com valores válidos")