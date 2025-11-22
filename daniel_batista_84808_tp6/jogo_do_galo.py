def jogo_do_galo():
    num_jogadas = 0
    tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def mostrar_tabuleiro(tab):
        print()
        print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
        print("---+---+---")
        print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
        print("---+---+---")
        print(f" {tab[6]} | {tab[7]} | {tab[8]} ")
        print()

    while True:
        mostrar_tabuleiro(tabuleiro)

        while True:
            try:
                pos_jog_1 = int(input("\njogador 1, insira posicao: "))
            except ValueError:
                print("Por favor insira um número válido.")
                continue
            if (tabuleiro[pos_jog_1 - 1] != 'o' and tabuleiro[pos_jog_1 - 1] != 'x'):
                tabuleiro[pos_jog_1 - 1] = 'o'
                break
            else:
                print("erro: posicao já preenchida")

        if ((tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 'o') or
            (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == 'o') or
            (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 'o') or
            (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == 'o') or
            (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 'o') or
            (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == 'o') or
            (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 'o') or
            (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 'o')):
            mostrar_tabuleiro(tabuleiro)
            print("Jogador 1 Ganhou!")
            break

        num_jogadas += 1
        if (num_jogadas == 9):
            print("Empate, atingimos o número máximo de jogadas (3x3)")
            break

        while True:
            try:
                jogador2 = int(input("\njogador 2, insira posicao: "))
            except ValueError:
                print("Por favor insira um número válido.")
                continue
            if (tabuleiro[jogador2 - 1] != 'x' and tabuleiro[jogador2 - 1] != 'o'):
                tabuleiro[jogador2 - 1] = 'x'
                break
            else:
                print("erro: posicao já preenchida")

        if ((tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 'x') or
            (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == 'x') or
            (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 'x') or
            (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == 'x') or
            (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 'x') or
            (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == 'x') or
            (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 'x') or
            (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 'x')):
            mostrar_tabuleiro(tabuleiro)
            print("Jogador 2 Ganhou!")
            break

        num_jogadas += 1


if __name__ == "__main__":
    jogo_do_galo()