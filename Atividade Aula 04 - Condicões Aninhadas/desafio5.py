#DESAFIO 05

#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: Todos os lados iguais
#Isósceles: Dois lados iguais
#Escaleno: Todos os lados diferentes

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
    if reta1 == reta2 == reta3:    
        print(f"É um triangulo equilátero. {reta1}, {reta2} e {reta3}")    
    elif reta1 != reta2 != reta3 != reta1:   
        print(f"É um triangulo escaleno. {reta1}, {reta2} e {reta3}")
    else:
        print(f"É um triangulo isósceles. {reta1}, {reta2} e {reta3}")
    
else:
    print(f"NÃO É um triangulo. {reta1}, {reta2} e {reta3}")
    
    
