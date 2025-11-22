import random

def ordenar_vetor(vetor):
    return sorted(vetor)

vetor = [random.randint(1, 100) for _ in range(10)]
print("Vetor:", vetor)
print("Vetor ordenado:", ordenar_vetor(vetor))