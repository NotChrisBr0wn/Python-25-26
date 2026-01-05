import random
import os
import time

# Cores e Emojis
RESET = "\033[0m"
COR_AGUA = "\033[94m"
COR_TIRO = "\033[91m"
COR_MISS = "\033[37m"
COR_BARCO = "\033[92m"

def criar_tabuleiro(tamanho=5):
    """Cria uma matriz vazia para o tabuleiro."""
    return [["~" for _ in range(tamanho)] for _ in range(tamanho)]

def mostrar_tabuleiro(tab, ocultar_barcos=False):
    print("\n      0   1   2   3   4") 
    print("    " + "—" * 21)
    for i, linha in enumerate(tab):
        exibicao = []
        for celula in linha:
            # 1º: Mostra sempre se já foi atingido
            if celula == "X":
                exibicao.append(f"{COR_TIRO}💥{RESET}")
            elif celula == "*":
                exibicao.append(f"{COR_MISS}⭕{RESET}")
            # 2º: Se não foi atingido, decide se mostra o barco ou água
            elif celula == "B":
                char = f"{COR_AGUA}💧{RESET}" if ocultar_barcos else f"{COR_BARCO}🚢{RESET}"
                exibicao.append(char)
            else:
                exibicao.append(f"{COR_AGUA}💧{RESET}")
        
        print(f"  {i} | " + " ".join(exibicao) + " |")
    print("    " + "—" * 21)

def colocar_barcos(tab, jogador_nome, auto=False):
    """Posiciona 3 barcos manual ou aleatoriamente."""
    num_barcos = 3
    count = 0
    while count < num_barcos:
        if auto:
            l, c = random.randint(0, 4), random.randint(0, 4)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"=== {jogador_nome}: POSICIONE OS SEUS BARCOS ===")
            mostrar_tabuleiro(tab)
            try:
                entrada = input(f"Barco {count+1}/3 - Linha e Coluna (ex: 4 4): ").split()
                l, c = int(entrada[0]), int(entrada[1])
            except (ValueError, IndexError):
                print("❌ Entrada inválida!"); time.sleep(1); continue

        if 0 <= l < 5 and 0 <= c < 5 and tab[l][c] == "~":
            tab[l][c] = "B"
            count += 1

def batalha_naval(save=None):
    """Função principal integrada com o sistema de saves do menu.py."""
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
        is_cpu = (modo == "1")
        colocar_barcos(tab2, "Computador" if is_cpu else "Jogador 2", auto=is_cpu)
        turno = 1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        is_cpu = (modo == "1")
        
        if turno == 1:
            nome_atacante, tab_alvo = "Jogador 1", tab2
        else:
            nome_atacante = "Computador" if is_cpu else "Jogador 2"
            tab_alvo = tab1

        print(f"=== VEZ DE: {nome_atacante} ===")
        
        # Inteligência Artificial (IA) corrigida
        if is_cpu and turno == 2:
            print("Computador está a escolher alvo...")
            time.sleep(1)
            while True:
                lin_tiro, col_tiro = random.randint(0, 4), random.randint(0, 4)
                # Garante que o computador não repita tiros em locais já atacados
                if tab_alvo[lin_tiro][col_tiro] in ["~", "B"]: 
                    break
        else:
            print("\nRADAR DO INIMIGO:")
            mostrar_tabuleiro(tab_alvo, ocultar_barcos=True)
            print("\n(S) Sair e Guardar")
            escolha = input("Ataque (Linha Coluna, ex: 4 4): ").strip().upper()

            if escolha == 'S':
                # Retorna dicionário para o menu.py guardar no arcade_data.json
                return {"tab1": tab1, "tab2": tab2, "turno": turno, "modo": modo}

            try:
                partes = escolha.split()
                lin_tiro, col_tiro = int(partes[0]), int(partes[1])
                if not (0 <= lin_tiro < 5 and 0 <= col_tiro < 5) or tab_alvo[lin_tiro][col_tiro] in ["X", "*"]:
                    print("⚠️ Alvo inválido ou já atacado!"); time.sleep(1); continue
            except (ValueError, IndexError):
                print("❌ Entrada inválida! Use: 0 0"); time.sleep(1); continue

        # Aplicação do tiro
        if tab_alvo[lin_tiro][col_tiro] == "B":
            print(f"💥 ACERTOU na Linha {lin_tiro}, Coluna {col_tiro}!")
            tab_alvo[lin_tiro][col_tiro] = "X"
        else:
            print(f"🌊 ÁGUA na Linha {lin_tiro}, Coluna {col_tiro}!")
            tab_alvo[lin_tiro][col_tiro] = "*"

        # Verificação de Vitória
        vitoria = not any("B" in linha for linha in tab_alvo)
        
        if vitoria:
            os.system('cls' if os.name == 'nt' else 'clear')
            mostrar_tabuleiro(tab_alvo, ocultar_barcos=False)
            print(f"\n🏆 VITÓRIA! {nome_atacante} afundou todos os barcos!")
            # Retorna strings compatíveis com a pontuação do menu.py
            return "vitoria_p1" if turno == 1 else "vitoria_p2"

        input("\nPrime Enter para passar o turno...")
        turno = 2 if turno == 1 else 1