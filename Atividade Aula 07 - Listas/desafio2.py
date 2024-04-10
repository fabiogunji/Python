# DESAFIO 02

# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já  exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados, em ordem crescente.

lstValores = []
contador = 1

while True:
    valor = int(input(f"Entre com o {contador}º número: "))
    
    if valor in lstValores:
        print(f"O valor {valor} já existe na lista.")
    else:
        lstValores.append(valor)
            
    contador += 1
    
    if (input("Deseja continuar? [S/N]: ").upper() == "S"):        
        continue
    else:
        break
    
print(f"Segue os valores da lista em ordem crescente {sorted(lstValores)}")       
    
    
    