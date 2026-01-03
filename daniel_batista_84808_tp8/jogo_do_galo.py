def jogo_do_galo(save=None):
    # Se houver save, usa-o. Se não, usa o tabuleiro inicial.
    tabuleiro = save if save else ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolo_atual = 'X' # Simplificação: começa sempre em X no load ou gere no menu
    
    while True:
        # Mostrar tabuleiro
        print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} \n---+---+---\n {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} \n---+---+---\n {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
        
        print("\n(S) Sair e Guardar")
        jogada = input(f"Jogador ({simbolo_atual}), escolha (1-9): ").strip().upper()

        if jogada == 'S':
            return tabuleiro # Retorna o estado da lista para o menu guardar

        try:
            pos = int(jogada) - 1
            if 0 <= pos <= 8 and tabuleiro[pos] not in ['X', 'O']:
                tabuleiro[pos] = simbolo_atual
            else: continue
        except: continue

        # Verificação de vitória
        vitorias = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        if any(tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == simbolo_atual for a, b, c in vitorias):
            return "vitoria" # Retorna sinal de vitória para o menu pontuar
            
        simbolo_atual = 'O' if simbolo_atual == 'X' else 'X'