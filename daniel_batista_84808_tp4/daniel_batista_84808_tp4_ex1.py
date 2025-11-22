valores = []

for i in range(10):
    valor = float(input(f"Digite o {i+1} valor: "))
    valores.append(valor)

maior = max(valores)
menor = min(valores)
dif = maior - menor

pares = 0
impares = 0

for i in valores:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Diferença entre maior e menor: {dif}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
