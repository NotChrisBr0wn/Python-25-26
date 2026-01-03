import random
import os

class Cores:
    RESET = "\033[0m"
    P1 = "\033[91m"  # Vermelho
    P2 = "\033[94m"  # Azul
    ESPECIAL = "\033[93m" # Amarelo
    BORDA = "\033[37m"

def mostrar_tabuleiro(p1_pos, p2_pos):
    # tabuleiro 8x8
    print("\n" + "═" * 41)
    for linha in range(8):
        row_str = "║"
        for coluna in range(8):
            casa = linha * 8 + coluna
            if casa > 63: break
            
            # Marcadores de jogadores
            if casa == p1_pos and casa == p2_pos:
                char = "XY" # Ambos na mesma casa
            elif casa == p1_pos:
                char = f"{Cores.P1}P1{Cores.RESET}"
            elif casa == p2_pos:
                char = f"{Cores.P2}P2{Cores.RESET}"
            elif casa in [6, 19, 25, 42, 58]: # Casas especiais
                char = f"{Cores.ESPECIAL}!!{Cores.RESET}"
            else:
                char = f"{casa:02d}"
            
            row_str += f" {char} ║"
        print(row_str)
        print("═" * 41 if linha == 7 else "╟" + "────╫" * 7 + "────╢")

def lanca_dado():
    return random.randint(1, 6)

def move_jogador(posicao_atual, valor_dado):
    nova_posicao = posicao_atual + valor_dado
    if nova_posicao > 63:
        nova_posicao = 63 - (nova_posicao - 63)
    return nova_posicao

def verificar_casas_especiais(pos):
    casas_especiais = {
        6: ("PONTE! Avança para a casa 12", 12),      
        19: ("POÇO! Ficas preso 1 turno", 19),      
        25: ("DADO! Salta para a casa 29", 29),     
        42: ("LABIRINTO! Recua para a casa 30", 30), 
        58: ("PRISÃO! Ficas preso 1 turno", 58),     
    }
    if pos in casas_especiais:
        return casas_especiais[pos]
    return None, pos

def jogo_da_gloria():
    p1_pos, p2_pos = 0, 0
    p1_skip, p2_skip = False, False
    turno = 1

    print("--- BEM-VINDO AO JOGO DA GLÓRIA ---")
    p1_nome = input("Nome Jogador 1: ") or "P1"
    p2_nome = input("Nome Jogador 2: ") or "P2"

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_tabuleiro(p1_pos, p2_pos)
        
        atual_nome = p1_nome if turno == 1 else p2_nome
        atual_pos = p1_pos if turno == 1 else p2_pos
        atual_skip = p1_skip if turno == 1 else p2_skip

        print(f"\n>>> Vez de {atual_nome} (Casa {atual_pos})")

        if atual_skip:
            print("⚠️ Estás preso! Perdes a vez.")
            if turno == 1: p1_skip = False
            else: p2_skip = False
        else:
            input("Pressiona Enter para lançar dado...")
            dado = lanca_dado()
            print(f"🎲 Dado: {dado}")
            
            nova_pos = move_jogador(atual_pos, dado)
            msg, final_pos = verificar_casas_especiais(nova_pos)
            
            if msg:
                print(f"⭐ {msg}")
                if "preso" in msg:
                    if turno == 1: p1_skip = True
                    else: p2_skip = True
            
            if turno == 1: p1_pos = final_pos
            else: p2_pos = final_pos

            if final_pos == 63:
                mostrar_tabuleiro(p1_pos, p2_pos)
                print(f"\n🏆 {atual_nome} VENCEU!")
                break

        turno = 2 if turno == 1 else 1
        input("\nPassar turno...")

if __name__ == "__main__":
    jogo_da_gloria()