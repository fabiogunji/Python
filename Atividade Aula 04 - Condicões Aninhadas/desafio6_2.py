from random import choice

opcoes = ["PEDRA", "PAPEL", "TESOURA"]

escolhaMaquina = choice(opcoes)

escolhaUsuario = input("Informe a sua escolha: ")

if escolhaMaquina  == escolhaUsuario:
    print(f"Ambos escolheram {escolhaMaquina}, portanto deu empate")
    
elif escolhaMaquina == "PEDRA" and escolhaUsuario == "TESOPURA":
    print(f"A máquina escolheu {escolhaMaquina}, portanto ela venceu")
