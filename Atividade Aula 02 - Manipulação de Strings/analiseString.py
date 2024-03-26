texto = "Curso de Python"
nome = "Fabio Jorge Gunji"

#Analisar o tamanho da frase
print(len(texto))
print(len(nome))

#Conta quantas vezesum caracter aparece
print(texto.count("o"))
print(nome.count("o"))

#Indica a posição de inicio de uma frase
print(texto.find("Python"))
print(texto.find("Java"))
print(nome.find("Gunji"))

# Verificando se posssui a palavra em uma frase
print("Python" in texto)
print("Silva" in nome)