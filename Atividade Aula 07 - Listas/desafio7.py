# DESAFIO 07

# Crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

    # |   1   |   2   |   3   |
    # |   4   |   5   |   6   |
    # |   7   |   8   |   9   |

# No final mostre a Matriz na tela, com a formatação correta.


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