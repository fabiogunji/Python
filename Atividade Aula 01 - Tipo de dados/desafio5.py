# DESAFIO 05

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar.
# Considere o dólar = R$ 5,00

valorCarteira = float(input("Informe quanto dinheiro você tem na carteira: "))
dolar = float(input("Informe o valor do Dólar: "))

compraDolar =  valorCarteira / dolar

print(f"Com R$ {float(valorCarteira)} você pode comprar US$ {compraDolar}, sendo que US$ 1,00 equivale a R$ {dolar}. ")
