#DESAFIO 04

#Faça um programa que leia uma frase pelo teclado e mostre:
frase = input("Entre com uma frase: ")

#Quantas vezes aparece a letra "A"
letraA = frase.upper().count("A")
fraseMaiuscula = frase.upper()

#Em que posição ela aparece a primeira vez
posAPri= fraseMaiuscula.find("A") + 1

#Em que posição ela aparece a ultima vezA
inverso = fraseMaiuscula[::-1]
ultPos = len(frase) - inverso.find("A")

#ou
#ultPos = fraseMaiuscula.rfind("A")+1

print(f"A frase é {frase} e primeira posição da letra A é {posAPri} e a última é a {ultPos}.")

