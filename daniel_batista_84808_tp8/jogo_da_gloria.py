import random
import os

# CORES
RESET = "\033[0m"
COR_P1 = "\033[91m"  # Vermelho
COR_P2 = "\033[94m"  # Azul

def mostrar_tabuleiro(p1_pos, p2_pos):
    # Tabuleiro 8x8 
    print("\n" + "═" * 41)
    for linha in range(8):
        row_str = "║"
        for coluna in range(8):
            casa = linha * 8 + coluna
            if casa > 63: break
            
            if casa == p1_pos and casa == p2_pos:
                char = "XY" 
            elif casa == p1_pos:
                char = f"{COR_P1}P1{RESET}"
            elif casa == p2_pos:
                char = f"{COR_P2}P2{RESET}"
            
            elif casa == 6:  char = "🌉" # Ponte
            elif casa == 19: char = "🕳️ " # Poço
            elif casa == 25: char = "🎲" # Dado
            elif casa == 42: char = "🌀" # Labirinto
            elif casa == 58: char = "🔒" # Prisão
            
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
        6: ("🌉 PONTE! Avança para a casa 12", 12),      
        19: ("🕳️  POÇO! Ficas preso 1 turno", 19),      
        25: ("🎲 DADO! Salta para a casa 29", 29),     
        42: ("🌀 LABIRINTO! Recua para a casa 30", 30), 
        58: ("🔒 PRISÃO! Ficas preso 1 turno", 58),     
    }
    if pos in casas_especiais:
        return casas_especiais[pos]
    return None, pos

def jogo_da_gloria(save=None):
    if save:
        p1_pos = save['p1_pos']
        p2_pos = save['p2_pos']
        p1_skip = save['p1_skip']
        p2_skip = save['p2_skip']
        turno = save['turno']
    else:
        p1_pos, p2_pos = 0, 0
        p1_skip, p2_skip = False, False
        turno = 1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_tabuleiro(p1_pos, p2_pos)
        
        atual_nome = "Jogador 1" if turno == 1 else "Jogador 2"
        atual_pos = p1_pos if turno == 1 else p2_pos
        atual_skip = p1_skip if turno == 1 else p2_skip

        print(f"\n>>> Vez de {atual_nome} (Casa {atual_pos})")
        print("Digite 'S' para SALVAR e SAIR ou Enter para lançar o dado.")
        comando = input("Escolha: ").strip().upper()

        if comando == 'S':
            return {
                "p1_pos": p1_pos, "p2_pos": p2_pos, 
                "p1_skip": p1_skip, "p2_skip": p2_skip, 
                "turno": turno
            }

        if atual_skip:
            print("⚠️ Estás preso! Perdes a vez.")
            if turno == 1: p1_skip = False
            else: p2_skip = False
        else:
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
                input("\nPrime Enter para voltar ao menu...")
                return "vitoria_p1" if turno == 1 else "vitoria_p2"

        turno = 2 if turno == 1 else 1
        input("\nPassar turno...")

if __name__ == "__main__":
    jogo_da_gloria()