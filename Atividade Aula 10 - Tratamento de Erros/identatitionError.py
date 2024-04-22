try:
    for elemento in range(1,10):
    print(elemento)
    
except RuntimeError:
    print("erro de fatal")
except SyntaxError:
    print("erro de sintaxe")
except IndentationError as err:
    print("Arruma a indentação", err)
