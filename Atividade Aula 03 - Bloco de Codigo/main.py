
try:
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Você é maior de idade, pode escolher a bebida.")    
    else:
        print("Você é menor de idade, não pode beber.")
except:
    print("Insira um valor correto!")

        