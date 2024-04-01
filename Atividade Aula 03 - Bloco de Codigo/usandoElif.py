prova = float(input("Digite a nota na prova do aluno (0 a 70): "))

atividade = float(input("Digite a média das notas das atividades (0 a 30): "))

# Nota prova      = 70% da media final
# Nota atividades = 30% da media final

mediaFinal = prova + atividade

print(mediaFinal)

if (mediaFinal >= 50):
    print(f" Aprovado! - Prova: {prova}, Atividade: {atividade} e {mediaFinal}")
elif (mediaFinal >= 40):
    print(f" Recuperação! - Prova: {prova}, Atividade: {atividade} e {mediaFinal}")
else:
    print(f" Reprovado! - Prova: {prova}, Atividade: {atividade} e {mediaFinal}")
    

