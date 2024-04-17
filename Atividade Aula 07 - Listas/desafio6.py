# DESAFIO 06

# Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e impares. 

# No final mostre os valores pares e impares e ordem crescente.

lstNumeros = []

for i in range(1,8):    
    valor = int(input(f"Entre com o {i}º vamlor numérico: "))
    
    if valor % 2 == 0:           
        lstNumeros.insert(i,valor)
    else:
        lstNumeros = lstNumeros + [valor]


print(lstNumeros)