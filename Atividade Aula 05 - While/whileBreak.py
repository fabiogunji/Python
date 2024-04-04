while True:
    continuar = input("Desaja continuar [S/N]: ").upper()
    
    if continuar == "N":
        print("Saindo do loop")
        break
    print("Continuando o loop")