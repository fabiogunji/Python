#DESAFIO 01

# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. 

# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
valorCasa = float(input("Entre com o valor da casa em reais: "))

salarioComprador = float(input("Entre com o salário do comprador: "))

anosPagamento = float(input("Entre com a quantidade de anos do financiamento: "))

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

limitePorCento = 0.3

limiteSalario = salarioComprador * limitePorCento

valorPrestacao = (valorCasa / (anosPagamento * 12))

if(valorPrestacao <= limiteSalario):
    print(f"O seu financiamento APROVADO! - R$ {valorCasa} em {anosPagamento} anos prestações de de R$ {valorPrestacao}")
else:
    print(f"O seu financiamento NEGADO! - R$ {valorCasa} em {anosPagamento} meses, limite de {limitePorCento}% a prestação SERIA de R$ {valorPrestacao}")

