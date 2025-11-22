def potencia(base, expoente):
    return base ** expoente

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = potencia(base, expoente)
print(f"{base}^{expoente}={resultado:.2f}")