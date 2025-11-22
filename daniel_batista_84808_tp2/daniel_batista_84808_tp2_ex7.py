letra = input("Introduza uma letra (L, D ou F): ")

if letra == 'L' or letra == 'l':
    print("Ligar")
elif letra == 'D' or letra == 'd':
    print("Desligar")
elif letra == 'F' or letra == 'f':
    print("Furar")
else:
    print("Erro!")