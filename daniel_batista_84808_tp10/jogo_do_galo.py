import os
import random
import time

def jogo_do_galo(save=None):
    # --- INICIALIZAÇÃO / CARREGAMENTO (Alínea c) ---
    if save:
        tabuleiro = save['tabuleiro']
        p1_simbolo = save['p1_simbolo']
        modo_cpu = save['modo_cpu']
        # Determina de quem é a vez com base no número de jogadas
        jogadas_feitas = sum(1 for x in tabuleiro if x in ['X', 'O'])
        simbolo_atual = 'X' if jogadas_feitas % 2 == 0 else 'O'
    else:
        tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== CONFIGURAÇÃO DO JOGO ===")
        print("1. Jogador vs Computador")
        print("2. Jogador vs Jogador")
        modo = input("Escolha o modo: ").strip()
        modo_cpu = True if modo == "1" else False
        
        while True:
            escolha = input("Jogador 1, queres ser 'X' ou 'O'? ").strip().upper()
            if escolha in ['X', 'O']:
                p1_simbolo = escolha
                break
            print("⚠️ Escolha inválida!")
        
        simbolo_atual = 'X' # O X começa sempre no Galo

    p2_simbolo = 'O' if p1_simbolo == 'X' else 'X'

    def mostrar_tabuleiro():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== JOGO DO GALO ===")
        print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
        print("---+---+---")
        print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
        print("---+---+---")
        print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n")
        
        nome_vez = "Jogador 1" if simbolo_atual == p1_simbolo else ("Computador" if modo_cpu else "Jogador 2")
        print(f"Vez de: {nome_vez} ({simbolo_atual})")
        print("---------------------------")
        print("Digite 'S' para SALVAR e SAIR.")
        print("---------------------------")

    def verificar_vitoria(s):
        v = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == s for a,b,c in v)

    # --- CICLO PRINCIPAL ---
    while True:
        mostrar_tabuleiro()
        
        # Lógica de Jogada (Humano vs CPU)
        if modo_cpu and simbolo_atual == p2_simbolo:
            print("Computador a pensar...")
            time.sleep(1)
            posicoes_livres = [i for i, x in enumerate(tabuleiro) if x not in ['X', 'O']]
            pos = random.choice(posicoes_livres)
        else:
            jogada = input("Escolha (1-9): ").strip().upper()
            if jogada == 'S': # Alínea b
                return {
                    'tabuleiro': tabuleiro, 
                    'p1_simbolo': p1_simbolo, 
                    'modo_cpu': modo_cpu
                }
            try:
                pos = int(jogada) - 1
                if not (0 <= pos <= 8 and tabuleiro[pos] not in ['X', 'O']):
                    print("❌ Posição ocupada ou inválida!"); time.sleep(1); continue
            except ValueError:
                print("❌ Opção inválida!"); time.sleep(1); continue

        tabuleiro[pos] = simbolo_atual

        # Verificar Fim de Jogo (Alínea d)
        if verificar_vitoria(simbolo_atual):
            mostrar_tabuleiro()
            if simbolo_atual == p1_simbolo:
                print("🏆 PARABÉNS! Jogador 1 venceu!")
                return "vitoria_p1"
            elif modo_cpu:
                print("🤖 O Computador venceu!")
                return "vitoria_cpu"
            else:
                print("🏆 PARABÉNS! Jogador 2 venceu!")
                return "vitoria_p2"

        if all(x in ['X', 'O'] for x in tabuleiro):
            mostrar_tabuleiro()
            print("🤝 Empate!")
            input("Prime Enter...")
            return "empate"

        # Troca de símbolo
        simbolo_atual = p2_simbolo if simbolo_atual == p1_simbolo else p1_simbolo

if __name__ == "__main__":
    jogo_do_galo()