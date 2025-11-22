import random

n = int(input("Digite o número de elementos da lista: "))
lista = [random.randint(1, 20) for _ in range(n)]
valor = int(input("Digite o valor a ser procurado na lista: "))

if valor in lista:
    print(f"O valor {valor} foi encontrado.")
else:
    print(f"O valor {valor} não foi encontrado.")

