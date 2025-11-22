def ler_disciplinas_notas():
    n = int(input("Quantas disciplinas tem neste semestre? "))
    for i in range(n):
        nome = input(f"Nome da disciplina {i+1}: ")
        nota = float(input("Nota esperada: "))
        sigla = "".join([palavra[0].upper() for palavra in nome.split()])
        print(f"{sigla} - {nota}")

ler_disciplinas_notas()
