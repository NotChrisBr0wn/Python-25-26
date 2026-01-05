import os

def quatro_em_linha(save=None):
    LINHAS, COLUNAS = 4, 6
    if save:
        tabuleiro = save['tab']
        turno = save['turno']
    else:
        tabuleiro = [[" " for _ in range(COLUNAS)] for _ in range(LINHAS)]
        turno = "X"

    def mostrar():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("  1   2   3   4   5   6")
        for linha in tabuleiro:
            print(f"| {' | '.join(linha)} |")
        print("-" * 25)

    def verificar_vitoria(p):
        # Horizontal, Vertical e Diagonais (lógica simplificada)
        for r in range(LINHAS):
            for c in range(COLUNAS - 4):
                if all(tabuleiro[r][c+i] == p for i in range(4)): return True
        for r in range(LINHAS - 4):
            for c in range(COLUNAS):
                if all(tabuleiro[r+i][c] == p for i in range(4)): return True
        return False

    while True:
        mostrar()
        print(f"Vez de {turno} | (S) Sair e Guardar")
        jogada = input("Coluna (1-6): ").strip().upper()

        if jogada == 'S':
            return {"tab": tabuleiro, "turno": turno}

        try:
            c = int(jogada) - 1
            for r in range(LINHAS-1, -1, -1):
                if tabuleiro[r][c] == " ":
                    tabuleiro[r][c] = turno
                    if verificar_vitoria(turno):
                        mostrar()
                        print(f"🏆 O Jogador {turno} venceu!")
                        input("Enter...")
                        return "vitoria"
                    turno = "O" if turno == "X" else "X"
                    break
        except: continue