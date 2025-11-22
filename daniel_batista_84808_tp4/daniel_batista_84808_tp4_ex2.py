import random

n = int(input("Digite o número de elementos da lista: "))
lista = [random.randint(1, 100) for _ in range(n)]

ordenada = sorted(lista)

print("Lista original:", lista)
print("Lista ordenada:", ordenada)