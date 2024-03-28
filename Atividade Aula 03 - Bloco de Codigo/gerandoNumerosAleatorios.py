
import random

nota1 = random.randint(1,10)
nota2 = random.randint(1,10)

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"APROVADO! - As notas são {nota1} e {nota2} e a sua média é {media}")
else:
    print(f"REPRPOVADO! - As notas são {nota1} e {nota2} e a sua média é {media}")