def trocar_nome(nome):
    partes = nome.strip().split()
    if len(partes) > 1:
        apelido = partes[-1]
        resto = " ".join(partes[:-1])
        return f"{apelido}, {resto}"
    else:
        return nome

nome = input("Digite o seu nome completo: ")
print("Nome:", trocar_nome(nome))
