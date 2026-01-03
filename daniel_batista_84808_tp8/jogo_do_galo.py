def jogo_do_galo():
    tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    while True:
        escolha = input("Jogador 1, queres ser 'X' ou 'O'? ").strip().upper()
        if escolha in ['X', 'O']:
            p1_simbolo = escolha
            break
        print("⚠️ Escolha inválida! Digita X ou O.")

    p2_simbolo = 'O' if p1_simbolo == 'X' else 'X'
    simbolo_atual = p1_simbolo
    num_jogadas = 0

    def mostrar_tabuleiro():
        print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
        print("---+---+---")
        print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
        print("---+---+---")
        print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n")

    while True:
        mostrar_tabuleiro()
        num_jogador = 1 if simbolo_atual == p1_simbolo else 2
        
        try:
            pos = int(input(f"Jogador {num_jogador} ({simbolo_atual}), escolha a posição (1-9): ")) - 1
            if 0 <= pos <= 8 and tabuleiro[pos] not in ['X', 'O']:
                tabuleiro[pos] = simbolo_atual
            else:
                print("❌ Posição inválida ou já ocupada!")
                continue
        except ValueError:
            print("❌ Por favor, insira um número de 1 a 9.")
            continue

        
        vitorias = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), 
            (0, 3, 6), (1, 4, 7), (2, 5, 8), 
            (0, 4, 8), (2, 4, 6)             
        ]
        
        venceu = any(tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == simbolo_atual for a, b, c in vitorias)

        if venceu:
            mostrar_tabuleiro()
            print(f"🏆 PARABÉNS! O Jogador {num_jogador} ({simbolo_atual}) ganhou!")
            break

        num_jogadas += 1
        if num_jogadas == 9:
            mostrar_tabuleiro()
            print("🤝 Empate! O jogo terminou sem vencedores.")
            break

        # 4. Alterna o símbolo para a próxima jogada
        simbolo_atual = p2_simbolo if simbolo_atual == p1_simbolo else p1_simbolo

if __name__ == "__main__":
    jogo_do_galo()