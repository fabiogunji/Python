# DESAFIOS

# DESAFIO 03

# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na sua posição correta de inserção (sem usar o sort()).
# No final mostre a lista ordenada na tela


lstValores = []
lstValoresBkp = []
lstOrdenada = []   
  
for i in range(5):
    lstValores.append(int(input(f"Entre com o {i}º número inteiro: ")))
    
lstValoresBkp.extend(lstValores)

for j in range(5):
    vlrMenor = min(lstValores)
    lstOrdenada.insert(j,vlrMenor)
    lstValores.remove(vlrMenor)    

print(f"A lista original é {lstValoresBkp} e a lista final é ficou {lstOrdenada}") 
   

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