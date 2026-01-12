import os
import random
import time

def quatro_em_linha(save=None):
    LINHAS, COLUNAS = 4, 6
    
    if save:
        tabuleiro = save['tab']
        turno = save['turno']
        modo_cpu = save.get('cpu', False)
    else:
        tabuleiro = [[" " for _ in range(COLUNAS)] for _ in range(LINHAS)]
        turno = "X"
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== CONFIGURAÇÃO: 4 EM LINHA ===")
        print("1. Jogador vs Computador")
        print("2. Jogador vs Jogador")
        modo = input("Escolha o modo: ").strip()
        modo_cpu = True if modo == "1" else False

    def mostrar():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("  1   2   3   4   5   6")
        for linha in tabuleiro:
            print(f"| {' | '.join(linha)} |")
        print("-" * 25)

    def verificar_vitoria(p):
        # Horizontal
        for r in range(LINHAS):
            for c in range(COLUNAS - 3):
                if all(tabuleiro[r][c+i] == p for i in range(4)): return True
        # Vertical
        for r in range(LINHAS - 3):
            for c in range(COLUNAS):
                if all(tabuleiro[r+i][c] == p for i in range(4)): return True
        # Diagonais
        for r in range(LINHAS - 3):
            for c in range(COLUNAS - 3):
                if all(tabuleiro[r+i][c+i] == p for i in range(4)): return True
                if all(tabuleiro[r+3-i][c+i] == p for i in range(4)): return True
        return False

    while True:
        mostrar()
        nome_turno = "Jogador 1" if turno == "X" else ("Computador" if modo_cpu else "Jogador 2")
        print(f"Vez de {nome_turno} ({turno}) | (S) Sair e Guardar")

        if modo_cpu and turno == "O":
            print("Computador a escolher coluna...")
            time.sleep(1)
            colunas_validas = [c for c in range(COLUNAS) if tabuleiro[0][c] == " "]
            if not colunas_validas: break # Empate
            c = random.choice(colunas_validas)
        else:
            jogada = input("Coluna (1-6): ").strip().upper()
            if jogada == 'S' or jogada == 's': 
                return {"tab": tabuleiro, "turno": turno, "cpu": modo_cpu}
            try:
                c = int(jogada) - 1
                if not (0 <= c < COLUNAS) or tabuleiro[0][c] != " ":
                    print("❌ Coluna inválida ou cheia!"); time.sleep(1); continue
            except: continue

        for r in range(LINHAS-1, -1, -1):
            if tabuleiro[r][c] == " ":
                tabuleiro[r][c] = turno
                break
            
        if verificar_vitoria(turno):
            mostrar()
            print(f"🏆 FIM DE JOGO: {nome_turno} VENCEU!")
            input("Prime Enter para voltar ao menu...")
            if turno == "X": return "vitoria_p1"
            return "vitoria_cpu" if modo_cpu else "vitoria_p2"

        # Verificar Empate
        if all(tabuleiro[0][c] != " " for c in range(COLUNAS)):
            mostrar()
            print("🤝 Empate! O tabuleiro está cheio.")
            input("Prime Enter...")
            return "empate"

        turno = "O" if turno == "X" else "X"