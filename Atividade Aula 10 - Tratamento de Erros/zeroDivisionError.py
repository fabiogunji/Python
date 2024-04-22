try:
    dvisao = 5 / 0
    print(dvisao)
    raise IndentationError("Errrrrrrou")
except SyntaxError:
    print("Erro de sintaxe") 
except ZeroDivisionError:
    print("Não existe divisão por zero")