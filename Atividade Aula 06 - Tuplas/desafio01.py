# DESAFIO 01

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

numerosExtenso = ("Zero","Hum", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "treze", "Quatrorze","Quinze","Dezeseis", "Dezessete","Dezoito", "Dezenove", "Vinte")

numero = int(input("Entre com um número inteiro entre 0 e 20: "))

if numero >= 0 and numero <= 20:
    print(f">>>>> O nome por extenso do número {numero} é {numerosExtenso[numero]}")
else:
    print("Entre com um número inteiro entre 0 e 20.")
