#DESAFIO 01

# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. 

# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
valorCasa = float(input("Entre com o valor da casa em R$: "))

salarioComprador = float(input("Entre com o salário do comprador R$: "))

anosPagamento = float(input("Entre com a quantidade de anos do financiamento: "))

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

limitePorCento = 0.3

limiteSalario = salarioComprador * limitePorCento

valorPrestacao = (valorCasa / (anosPagamento * 12))

if(valorPrestacao <= limiteSalario):
    print(f"O seu financiamento foi APROVADO! - R$ {valorCasa:.2f} em {anosPagamento} anos prestações de de R$ {valorPrestacao:.2f}")
else:
    print(f"O seu financiamento foi NEGADO! - R$ {valorCasa:.2f} em {anosPagamento} meses, limite de {limitePorCento}% a prestação SERIA de R$ {valorPrestacao:.2f}")

