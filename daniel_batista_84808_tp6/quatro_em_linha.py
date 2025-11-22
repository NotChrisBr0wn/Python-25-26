num_jogadas = 0
tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

def mostrar_tabuleiro(tab):
    print()
    print(f" {tab[0]} | {tab[1]} | {tab[2]} | {tab[3]} |  {tab[4]} |")
    print("--------------------")
    print(f" {tab[5]} | {tab[6]} | {tab[7]} | {tab[8]} | {tab[9]} |")
    print("--------------------")
    print(f" {tab[10]}| {tab[11]}| {tab[12]}| {tab[12]}| {tab[13]} |")
    print("--------------------")
    print(f" {tab[14]}| {tab[15]}| {tab[16]}| {tab[17]}| {tab[18]} |")
    print()

while True:
    mostrar_tabuleiro(tabuleiro)

    while True:
        pos_jog_1 = int(input("\njogador 1, insira posicao: "))
        if (tabuleiro[pos_jog_1 - 1] != 'o' and tabuleiro[pos_jog_1 - 1] != 'x'):
            tabuleiro[pos_jog_1 - 1] = 'o'
            break
        else:
            print ("erro: posicao já preenchida")
    if ((tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == tabuleiro[3] == 'o') or
        (tabuleiro[4] == tabuleiro[5] == tabuleiro[6] == tabuleiro[7] == 'o') or
        (tabuleiro[8] == tabuleiro[9] == tabuleiro[10] == tabuleiro[11] == 'o') or
        (tabuleiro[12] == tabuleiro[13] == tabuleiro[14] == tabuleiro[15] == 'o') or
        (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == tabuleiro[12] == 'o') or
        (tabuleiro[1] == tabuleiro[5] == tabuleiro[9] == tabuleiro[13] == 'o') or
        (tabuleiro[2] == tabuleiro[6] == tabuleiro[10] == tabuleiro[14] == 'o') or
        (tabuleiro[3] == tabuleiro[7] == tabuleiro[11] == tabuleiro[15] == 'o') or
        (tabuleiro[0] == tabuleiro[5] == tabuleiro[10] == tabuleiro[15] == 'o') or
        (tabuleiro[3] == tabuleiro[6] == tabuleiro[9] == tabuleiro[12] == 'o')):
        
        mostrar_tabuleiro(tabuleiro)
        print("Jogador 1 Ganhou!")
        break

    num_jogadas += 1
    if (num_jogadas == 20):
        print("Empate, atingimos o número máximo de jogadas (4x5)")
        break

    while True:
        jogador2 = int(input("\njogador 2, insira posicao: "))
        if (tabuleiro[jogador2 - 1] != 'x' and tabuleiro[jogador2 - 1] != 'o'):
            tabuleiro[jogador2 - 1] = 'x'
            break
        else:
            print ("erro: posicao já preenchida")
    
    if ((tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == tabuleiro[3] == 'x') or
        (tabuleiro[4] == tabuleiro[5] == tabuleiro[6] == tabuleiro[7] == 'x') or
        (tabuleiro[8] == tabuleiro[9] == tabuleiro[10] == tabuleiro[11] == 'x') or
        (tabuleiro[12] == tabuleiro[13] == tabuleiro[14] == tabuleiro[15] == 'x') or
        (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == tabuleiro[12] == 'x') or
        (tabuleiro[1] == tabuleiro[5] == tabuleiro[9] == tabuleiro[13] == 'x') or
        (tabuleiro[2] == tabuleiro[6] == tabuleiro[10] == tabuleiro[14] == 'x') or
        (tabuleiro[3] == tabuleiro[7] == tabuleiro[11] == tabuleiro[15] == 'x') or
        (tabuleiro[0] == tabuleiro[5] == tabuleiro[10] == tabuleiro[15] == 'x') or
        (tabuleiro[3] == tabuleiro[6] == tabuleiro[9] == tabuleiro[12] == 'x')):
        
        mostrar_tabuleiro(tabuleiro)
        print("Jogador 2 Ganhou!")
        break

    num_jogadas += 1