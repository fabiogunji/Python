# DESAFIO 05

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

from tabulate import tabulate

produtos = (["Bala","0.30"],["suco","4.10"],["Sorvete","32.30"],["Paçoca","1.5"],["M&M","11.30"],["Milka","18.30"])            
print(tabulate(produtos, headers=["Produto", "Preço"]))
