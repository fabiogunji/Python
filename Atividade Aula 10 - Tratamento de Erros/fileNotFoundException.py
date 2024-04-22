try:
    with open("exemplo.txt","r") as arquivo:
        conteudo = arquivo.read()        
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não existe")
    