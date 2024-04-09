# DESAFIO 03

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro Serie B de Futebol, na ordem de colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Santos.

serieB = ("Amazonas","América-MG","Avaí","Botafogo-SP","Brusque","Ceará","Chapecoense","Coritiba","CRB","Goiás","Guarani","Ituano","Mirassol","Novorizontino","Operário","Paysandu","Ponte Preta","Santos","Sport","Vila Nova")

print(f"A) Apenas os 5 primeiros colocados: {serieB[0:5]}")
print(f"B) Os últimos 4 colocados da tabela: {serieB[-5:]} ")
print(f"C) Uma lista com os times em ordem alfabética: {sorted(serieB)}")
posicaoSantos = serieB.index("Santos")
print(f"D) Em que posição na tabela está o time do Santos: Posição {posicaoSantos}")