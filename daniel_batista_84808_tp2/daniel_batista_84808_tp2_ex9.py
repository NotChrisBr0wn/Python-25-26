n = int(input("Introduza o número de alunos na turma: "))

idades = []
alturas = []

for i in range(n):
    print(f"Aluno {i + 1}:")
    idade = int(input("Idade: "))
    altura = float(input("Altura (em metros): "))
    
    idades.append(idade)
    alturas.append(altura)

media_idades = sum(idades) / n
media_alturas = sum(alturas) / n

altura_max = max(alturas)

idade_min = min(idades)

# Mostra os resultados
print("\n=== Resultados ===")
print(f"Média das idades: {media_idades:.1f} anos")
print(f"Média das alturas: {media_alturas:.2f} m")
print(f"Altura do aluno mais alto: {altura_max:.2f} m")
print(f"Idade do aluno mais novo: {idade_min} anos")
