def ler_valores():
    vetor = []
    for i in range(10):
        valor = int(input(f"Digite o {i+1}º valor: "))
        vetor.append(valor)
    return vetor

def diferenca_maior_menor(vetor):
    return max(vetor) - min(vetor)

def pares_impares(vetor):
    pares = sum(1 for i in vetor if i % 2 == 0)
    impares = len(vetor) - pares
    return pares, impares

valores = ler_valores()
print(f"Diferença entre o maior e o menor valor: {diferenca_maior_menor(valores)}")

par,impar = pares_impares(valores)
print(f"Números pares: {par}, Números ímpares: {impar}")
