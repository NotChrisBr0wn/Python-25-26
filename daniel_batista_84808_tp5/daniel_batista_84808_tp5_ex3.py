def menor_algarismo(numero):
    numero = abs(numero)
    digitos = [int(d) for d in str(numero)]
    return min(digitos)

n = int(input("Digite um número inteiro: "))
print(f"O menor algarismo é {menor_algarismo(n)}")
