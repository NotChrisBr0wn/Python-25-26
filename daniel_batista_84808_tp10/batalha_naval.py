import random
import os
import time

# Cores e Emojis para o terminal
RESET = "\033[0m"
COR_AGUA = "\033[94m"
COR_TIRO = "\033[91m"
COR_MISS = "\033[37m"
COR_BARCO = "\033[92m"

def criar_tabuleiro(tamanho=5):
    return [["~" for _ in range(tamanho)] for _ in range(tamanho)]

def mostrar_tabuleiro(tab, ocultar_barcos=False):
    print("\n       1  2  3  4  5") 
    print("    " + "—" * 18)
    for i, linha in enumerate(tab):
        exibicao = []
        for celula in linha:
            if celula == "~":
                exibicao.append(f"{COR_AGUA}💧{RESET}")
            elif celula == "B":
                char = f"{COR_AGUA}💧{RESET}" if ocultar_barcos else f"{COR_BARCO}🚢{RESET}"
                exibicao.append(char)
            elif celula == "X":
                exibicao.append(f"{COR_TIRO}💥{RESET}")
            elif celula == "*":
                exibicao.append(f"{COR_MISS}⭕{RESET}")
        print(f"  {i} | " + " ".join(exibicao) + " |")
    print("    " + "—" * 18)

def colocar_barcos(tab, nome, auto=False):
    num = 5
    count = 0
    while count < num:
        if auto:
            l, c = random.randint(0, 4), random.randint(0, 4)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"=== {nome}: POSICIONE OS SEUS BARCOS ===")
            mostrar_tabuleiro(tab)
            try:
                entrada = input(f"Barco {count+1}/5 (Linha Coluna): ").split()
                l, c = int(entrada[0]), int(entrada[1])
            except: continue
        
        if 0 <= l < 5 and 0 <= c < 5 and tab[l][c] == "~": # Verifica se a posição está livre
            tab[l][c] = "B"
            count += 1

def batalha_naval(save=None):
    if save:
        tab1, tab2 = save['tab1'], save['tab2']
        turno, modo = save['turno'], save['modo']
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== MODO DE JOGO ===")
        print("1. Jogador vs Computador")
        print("2. Jogador vs Jogador")
        modo = input("Escolha: ").strip()
        
        tab1, tab2 = criar_tabuleiro(), criar_tabuleiro()
        colocar_barcos(tab1, "Jogador 1")
        colocar_barcos(tab2, "Adversário", auto=(modo == "1"))
        turno = 1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        nome_atacante = "Jogador 1" if turno == 1 else ("Computador" if modo == "1" else "Jogador 2")
        tab_alvo = tab2 if turno == 1 else tab1
        
        print(f"=== VEZ DE: {nome_atacante} ===")
        
        if modo == "1" and turno == 2:
            print("Computador a atacar...")
            time.sleep(1)
            while True:
                l, c = random.randint(0, 4), random.randint(0, 4)
                if tab_alvo[l][c] in ["~", "B"]: break
        else:
            print("\nRADAR DO INIMIGO:")
            mostrar_tabuleiro(tab_alvo, ocultar_barcos=True)
            print("\n(S) SALVAR E SAIR")
            escolha = input("Ataque (Linha Coluna): ").strip().upper()

            if escolha == 'S' or escolha == 's':
                return {"tab1": tab1, "tab2": tab2, "turno": turno, "modo": modo}

            try:
                partes = escolha.split()
                l, c = int(partes[0]), int(partes[1])
            except: continue

        if tab_alvo[l][c] == "B":
            print(f"💥 ACERTOU em ({l}, {c})!")
            tab_alvo[l][c] = "X"
        else:
            print(f"🌊 ÁGUA em ({l}, {c})!")
            tab_alvo[l][c] = "*"

        if sum(row.count("B") for row in tab_alvo) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"🏆 VITÓRIA! {nome_atacante} venceu!")
            if turno == 1: return "vitoria_p1"
            return "vitoria_cpu" if modo == "1" else "vitoria_p2"

        input("\nPrime Enter...")
        turno = 2 if turno == 1 else 1