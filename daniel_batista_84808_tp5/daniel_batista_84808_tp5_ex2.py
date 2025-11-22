def maior_algarismo(numero):
    numero = abs(numero) 
    digitos = [int(d) for d in str(numero)]
    return max(digitos)

n = int(input("Digite um número inteiro: "))
print(f"O maior algarismo é {maior_algarismo(n)}")