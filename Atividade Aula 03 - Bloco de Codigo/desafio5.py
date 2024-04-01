# DESAFIO 05

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = int(input("Entre com o comprimento da reta 1: ")) #a
reta2 = int(input("Entre com o comprimento da reta 2: ")) #b
reta3 = int(input("Entre com o comprimento da reta 3: ")) #c


# Condições Necessárias:
# a + b > c
# a + c > b
# b + c > a

ab = reta1 + reta2
ac = reta1 + reta3
bc = reta2 + reta3

if (ab > reta3) and (ac > reta2) and (bc > reta1):
    print(f"É um triangulo. {reta1}, {reta2} e {reta3}")
else:
    print(f"NÃO É um triangulo. {reta1}, {reta2} e {reta3}")
    
    

     
    