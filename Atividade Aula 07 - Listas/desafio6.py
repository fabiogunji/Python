# DESAFIO 06

# Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e impares. 

# No final mostre os valores pares e impares e ordem crescente.

lstNumeros = []
lstPares = []
lstImpares = []
contador = 0

for i in range(0,7):    
    valor = int(input(f"Entre com um valor numérico: "))  
    if valor % 2 != 0:                  
        lstNumeros.insert(contador,valor)
        contador += 1 
    else:
       lstNumeros.insert(len(lstNumeros)+1,valor)    

for n in lstNumeros:
    if n % 2 != 0:
        lstImpares.append(n)
    else:
        lstPares.append(n)
        

print(f"Lista de números separados por par e impar: {lstNumeros}")
print(f"Lista impar em ordem crescente: {sorted(lstImpares)} ")
print(f"Lista par em ordem crescente: {sorted(lstPares)} ")