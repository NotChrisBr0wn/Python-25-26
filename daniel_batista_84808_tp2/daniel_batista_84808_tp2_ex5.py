nota = float(input("Introduza o valor da nota: "))

if nota <= 9.5 and nota > 0:
    print("Reprovado!")
elif nota < 0 or nota > 20:
    print("Erro, introduza uma nota entre 0-20.")
else:
    print("Aprovado!")