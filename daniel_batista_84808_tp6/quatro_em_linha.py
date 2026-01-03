def quatro_em_linha():
    # Matriz do tabuleiro 4x5
    linhas = 4
    colunas = 5
    tabuleiro = [[" " for _ in range(colunas)] for _ in range(linhas)]

    def mostrar_tabuleiro():
        print("\n  1   2   3   4   5")
        for linha in tabuleiro:
            print(f"| {' | '.join(linha)} |") 
            print("-" * 21)

    def obter_linha_disponivel(col):
        # Verifica espaço livre
        for r in range(linhas - 1, -1, -1):
            if tabuleiro[r][col] == " ":
                return r
        return None

    def verificar_vitoria(p):
        for r in range(linhas):
            for c in range(colunas - 3):
                if tabuleiro[r][c] == p and tabuleiro[r][c+1] == p and tabuleiro[r][c+2] == p and tabuleiro[r][c+3] == p:
                    return True
        for r in range(linhas - 3):
            for c in range(colunas):
                if tabuleiro[r][c] == p and tabuleiro[r+1][c] == p and tabuleiro[r+2][c] == p and tabuleiro[r+3][c] == p:
                    return True
        for r in range(3, linhas):
            for c in range(colunas - 3):
                if tabuleiro[r][c] == p and tabuleiro[r-1][c+1] == p and tabuleiro[r-2][c+2] == p and tabuleiro[r-3][c+3] == p:
                    return True
        for r in range(linhas - 3):
            for c in range(colunas - 3):
                if tabuleiro[r][c] == p and tabuleiro[r+1][c+1] == p and tabuleiro[r+2][c+2] == p and tabuleiro[r+3][c+3] == p:
                    return True
        return False

    jogador = "o"
    jogadas_totais = 0

    while True:
        mostrar_tabuleiro()
        try:
            col_input = int(input(f"\nJogador {jogador}, escolha a coluna (1-5): ")) - 1
            if col_input < 0 or col_input >= colunas:
                print("Coluna inválida! Escolha entre 1 e 5.")
                continue
        except ValueError:
            print("Por favor, insira um número.")
            continue

        linha = obter_linha_disponivel(col_input)

        if linha is not None:
            tabuleiro[linha][col_input] = jogador
            jogadas_totais += 1
            
            if verificar_vitoria(jogador):
                mostrar_tabuleiro()
                print(f"\nParabéns! O Jogador {jogador} venceu!")
                break
            
            if jogadas_totais == linhas * colunas:
                mostrar_tabuleiro()
                print("\nEmpate! O tabuleiro está cheio.")
                break
            
            # Troca de jogador
            jogador = "x" if jogador == "o" else "o"
        else:
            print("Essa coluna já está cheia! Tenta outra.")

if __name__ == "__main__":
    quatro_em_linha()