# DESAFIO 08

# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


matriz= [[0,0,0],[1,1,1],[2,2,2]]
c=0

for i in range (0,3):
   
    for j in matriz[i]:
       
        if c==3:
            c=0
                 
        numero= int(input(f"Digite um valor para[{i},{c}]: "))
       
        matriz[i][c]=numero    
        c +=1
        
print(matriz[0])
print(matriz[1])
print(matriz[2])