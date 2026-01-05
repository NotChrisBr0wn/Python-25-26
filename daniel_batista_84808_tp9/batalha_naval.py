import random
import os

# Variáveis de cores simples (sem classes)
RESET = "\033[0m"
COR_AGUA = "\033[94m"  # Azul para o mar
COR_TIRO = "\033[91m"  # Vermelho para o X (Acerto)
COR_MISS = "\033[37m"  # Cinza para o O (Falha/Água)
COR_BARCO = "\033[92m" # Verde para o B (Teus barcos)

def criar_tabuleiro(tamanho=5):
    """Cria uma matriz vazia para o jogo."""
    return [["~" for _ in range(tamanho)] for _ in range(tamanho)]

def mostrar_tabuleiro(tab, ocultar_barcos=False):
    """Desenha o tabuleiro alinhado com os números das colunas."""
    # Reduzimos o espaço inicial para alinhar o 0 com o primeiro emoji
    print("\n      0   1   2   3   4") 
    print("    " + "—" * 21)
    
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
        
        # O SEGREDO ESTÁ AQUI: 
        # Usamos apenas um espaço " " no join para os emojis ficarem mais juntos
        print(f"  {i} | " + " ".join(exibicao) + " |")
    
    print("    " + "—" * 21)

def batalha_naval(save=None):
    TAMANHO = 5
    NUM_BARCOS = 3
    
    if save:
        tab1, tab2 = save['tab1'], save['tab2']
        turno, modo = save['turno'], save['modo']
    else:
        # Configuração inicial
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== BATALHA NAVAL ===")
        print("1. Jogador vs Computador")
        print("2. Jogador vs Jogador")
        modo = input("Escolha o modo: ")
        
        tab1, tab2 = criar_tabuleiro(TAMANHO), criar_tabuleiro(TAMANHO)
        
        # Colocação automática (Alínea A - Computador escolhe)
        colocar_barcos_auto(tab1, NUM_BARCOS)
        colocar_barcos_auto(tab2, NUM_BARCOS)
        turno = 1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== TURNO DO JOGADOR {turno} ===")
        
        # O Jogador ataca o tabuleiro do adversário
        tab_defesa = tab2 if turno == 1 else tab1
        
        print("\nRADAR DO INIMIGO (Onde estás a disparar):")
        mostrar_tabuleiro(tab_defesa, ocultar_barcos=True)
        
        print("\n(S) Sair e Guardar")
        escolha = input("Coordenadas de Ataque (ex: 0 0): ").strip().upper()

        if escolha == 'S':
            return {"tab1": tab1, "tab2": tab2, "turno": turno, "modo": modo}

        try:
            # Correção do erro 0 0: split garante que pega os dois números separadamente
            partes = escolha.split()
            l, c = int(partes[0]), int(partes[1])

            if not (0 <= l < TAMANHO and 0 <= c < TAMANHO):
                print("⚠️ Coordenadas fora do mapa!")
                input("Enter..."); continue

            if tab_defesa[l][c] == "B":
                print("🔥 DIRETO! Afundaste uma parte!")
                tab_defesa[l][c] = "X"
            elif tab_defesa[l][c] == "~":
                print("🌊 Água... Tentaste acertar nos peixes.")
                tab_defesa[l][c] = "*"
            else:
                print("Já disparaste nesta posição!")
                input("Enter..."); continue
            
            # Verificar vitória: se não sobrarem barcos "B"
            if sum(row.count("B") for row in tab_defesa) == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                mostrar_tabuleiro(tab_defesa, ocultar_barcos=False)
                print(f"\n🏆 PARABÉNS! JOGADOR {turno} VENCEU A BATALHA!")
                input("Enter..."); return f"vitoria_p{turno}"

            turno = 2 if turno == 1 else 1
            
        except (ValueError, IndexError):
            print("❌ Entrada inválida! Escreve dois números (ex: 0 0).")
            input("Enter...")

def colocar_barcos_auto(tab, num):
    """Coloca barcos aleatoriamente no tabuleiro."""
    c = 0
    while c < num:
        l, col = random.randint(0, 4), random.randint(0, 4)
        if tab[l][col] == "~":
            tab[l][col] = "B"
            c += 1