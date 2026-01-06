import random
import os
import time

def minesweeper(save=None):
    L, C, BOMBAS = 5, 5, 3
    
    if save:
        real, visivel = save['real'], save['visivel']
        modo = save.get('modo', 'cpu')
    else:
        # --- ESCOLHA DE MODO (Alínea a) ---
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== MINESWEEPER ===")
        print("1. Contra Computador (Bombas Aleatórias)")
        print("2. Contra Jogador 2 (Oponente coloca as bombas)")
        opcao = input("Escolha (1-2): ").strip()
        
        modo = '2p' if opcao == '2' else 'cpu'
        real = [["0" for _ in range(C)] for _ in range(L)]
        visivel = [["?" for _ in range(C)] for _ in range(L)]

        if modo == '2p':
            bombas_colocadas = 0
            while bombas_colocadas < BOMBAS:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"=== CONFIGURAÇÃO JOGADOR 2 ({bombas_colocadas}/{BOMBAS} bombas) ===")
                for i, row in enumerate(real):
                    print(f"{i} | {' '.join(['X' if c=='B' else '.' for c in row])} |")
                
                try:
                    coord = input(f"\nOnde colocar a bomba {bombas_colocadas + 1} (Linha Coluna): ").split()
                    rl, rc = int(coord[0]), int(coord[1])
                    if real[rl][rc] != "B":
                        real[rl][rc] = "B"
                        bombas_colocadas += 1
                    else:
                        print("⚠️ Já existe uma bomba aí!"); time.sleep(1)
                except:
                    print("❌ Coordenadas inválidas!"); time.sleep(1)
        else:
            for _ in range(BOMBAS):
                while True:
                    rl, rc = random.randint(0, L-1), random.randint(0, C-1)
                    if real[rl][rc] != "B":
                        real[rl][rc] = "B"
                        break

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo = "MODO 2P" if modo == '2p' else "MODO CPU"
        print(f"=== MINESWEEPER ({titulo}) ===")
        print("\n   " + " ".join(str(i) for i in range(C)))
        print("  " + "—" * (C * 2 + 1))
        for i, row in enumerate(visivel):
            print(f"{i} | {' '.join(row)} |")
        print("  " + "—" * (C * 2 + 1))
        
        print("\n(S) SALVAR E SAIR")
        escolha = input("Revelar (Linha Coluna): ").strip().upper()
        
        if escolha == 'S':
            return {"real": real, "visivel": visivel, "modo": modo}

        try:
            partes = escolha.split()
            l, c = int(partes[0]), int(partes[1])
            
            if real[l][c] == "B":
                os.system('cls' if os.name == 'nt' else 'clear')
                for rl in range(L):
                    for rc in range(C):
                        if real[rl][rc] == "B": visivel[rl][rc] = "💥"
                
                print("=== GAME OVER ===")
                for row in visivel: print(f"| {' '.join(row)} |")
                
                if modo == '2p':
                    print("\n💀 Explodiste! O ponto vai para o Jogador 2.")
                    input("Prime Enter...")
                    return "vitoria_p2"
                else:
                    print("\n💀 Explodiste! O ponto vai para a CPU.")
                    input("Prime Enter...")
                    return "vitoria_cpu"

            visivel[l][c] = "." 

            if sum(r.count("?") for r in visivel) == BOMBAS:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("🏆 PARABÉNS! Limpaste o campo com sucesso!")
                input("Prime Enter...")
                return "vitoria_p1"
                
        except:
            continue