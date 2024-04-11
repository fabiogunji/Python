# DESAFIOS

# DESAFIO 03

# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na sua posição correta de inserção (sem usar o sort()).
# No final mostre a lista ordenada na tela


lstValores = []
  
  
for i in range(5):
    valores = int(input(f"Entre com o {i}º número inteiro: "))
    
    lstOrdenada = []   
  
    for chave, valor in enumerate(lstOrdenada):
        print(f" chave {chave} e {valor}")        
  
'''
for i in range(5):
    lstValores.append(int(input(f"Entre com o {i}º número inteiro: ")))

#print(lstValores)

for numero in lstValores:

    for chave, valor in enumerate(lstValores):
        print(f" chave {chave} e {valor}")        
        
        if numero < valor:
            lstOrdenada.insert(chave,numero)
        else:
            lstOrdenada.append(numero)

print(lstOrdenada)
'''          
   

# Resolução Pedro

'''
lista = []

for c in range(0,5):    
    n = int(input("Digite um valor: "))

    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):  
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f"Adicionado na posição {pos} da lista")
                break
            pos += 1

print(f"Os valores digitados em ordem foram {lista}")
'''    