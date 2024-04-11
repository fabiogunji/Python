# Lista de dicionario

personagens = [
    {
        "Nome":"Bob",
        "Sobrenome":"Esponja",
        "Idade":10        
    },
    {
        "Nome":"Jhony",
        "Sobrenome":"Bravo",
        "Idade":35
    }
]

print(type(personagens))
print(personagens[0])


primeiroRegistro = personagens[0]
print(primeiroRegistro)

print(primeiroRegistro["Nome"])
#ou
print(personagens[0].get("Nome"))
