def procurar_numero(vetor, numero):
    return numero in vetor

valores = [int(x) for x in input("Digite uma seqûencia de números: ").split()]
n = int(input("Digite o número a procurar: "))

if procurar_numero(valores, n):
    print("true")
else:
    print("false")
