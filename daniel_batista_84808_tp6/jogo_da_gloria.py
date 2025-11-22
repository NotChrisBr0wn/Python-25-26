import random
import os

# Carrega o tabuleiro do ficheiro txt
def load_board():
    board_path = os.path.join(os.path.dirname(__file__), "board.txt")
    try:
        with open(board_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Ficheiro do tabuleiro não encontrado!"

# Tabuleiro do jogo
BOARD_ASCII = load_board()

def print_board():
    """Mostra o tabuleiro do ficheiro txt"""
    print(BOARD_ASCII)

def lanca_dado():
    """Simula um lançamento de dado (1-6)"""
    return random.randint(1, 6)

def move_player(current_pos, dice_value):
    """Calcula a nova posição após lançar o dado"""
    new_pos = current_pos + dice_value
    if new_pos > 63:
        new_pos = 63 - (new_pos - 63)  # Volta atrás se ultrapassar
    return new_pos

def check_special_squares(pos):
    """Verifica se o jogador caiu numa casa especial"""
    special_squares = {
        6: ("PONTE!", 12),      # Ponte vai para 12
        19: ("POÇO!", 0),       # Poço, perde turno
        25: ("DADO!", 29),      # Dado, avança para 29
        42: ("LABIRINTO!", 30), # Labirinto volta para 30
        58: ("PRISÃO!", 0),     # Prisão, perde turno
    }
    
    if pos in special_squares:
        name, effect_pos = special_squares[pos]
        if effect_pos == 0:
            return name, pos, True  # Perde próximo turno
        else:
            return name, effect_pos, False
    return None, pos, False

def jogo_da_gloria():
    print("\n" + "="*60)
    print("BEM VINDO AO JOGO DA GLÓRIA!")
    print("="*60)
    
    # Inicialização dos jogadores
    player1_name = input("Nome do Jogador 1: ").strip() or "Jogador 1"
    player2_name = input("Nome do Jogador 2: ").strip() or "Jogador 2"
    
    player1_pos = 0
    player2_pos = 0
    player1_skip = False
    player2_skip = False
    
    current_player = 1
    
    print(f"\n{player1_name} vs {player2_name}")
    print("Objetivo: Ser o primeiro a chegar à casa 63!")
    input("Pressione Enter para começar...")
    
    turn_count = 0
    
    while True:
        turn_count += 1
        print("\n" + "="*60)
        print_board()
        print("="*60)
        
        if current_player == 1:
            print(f"\n🎮 TURNO DE {player1_name.upper()} (Casa {player1_pos})")
            
            if player1_skip:
                print(f"⚠️  {player1_name} está preso/enfiado e perde este turno!")
                player1_skip = False
                current_player = 2
                input("Pressione Enter para continuar...")
                continue
            
            input(f"{player1_name}, pressione Enter para lançar o dado...")
            dice = lanca_dado()
            print(f"🎲 Saiu: {dice}")
            
            old_pos = player1_pos
            player1_pos = move_player(player1_pos, dice)
            
            special, player1_pos, skip = check_special_squares(player1_pos)
            if special:
                print(f"⭐ Caiu em: {special} → Casa {player1_pos}")
                player1_skip = skip
            else:
                print(f"➜ Moveu-se para a casa {player1_pos}")
            
            if player1_pos == 63:
                print(f"\n🏆 {player1_name} chegou à casa da Glória! 🏆")
                print(f"PARABÉNS! {player1_name} GANHOU O JOGO!")
                break
            
            current_player = 2
        
        else:
            print(f"\n🎮 TURNO DE {player2_name.upper()} (Casa {player2_pos})")
            
            if player2_skip:
                print(f"⚠️  {player2_name} está preso/enfiado e perde este turno!")
                player2_skip = False
                current_player = 1
                input("Pressione Enter para continuar...")
                continue
            
            input(f"{player2_name}, pressione Enter para lançar o dado...")
            dice = lanca_dado()
            print(f"🎲 Saiu: {dice}")
            
            old_pos = player2_pos
            player2_pos = move_player(player2_pos, dice)
            
            special, player2_pos, skip = check_special_squares(player2_pos)
            if special:
                print(f"⭐ Caiu em: {special} → Casa {player2_pos}")
                player2_skip = skip
            else:
                print(f"➜ Moveu-se para a casa {player2_pos}")
            
            if player2_pos == 63:
                print(f"\n🏆 {player2_name} chegou à casa da Glória! 🏆")
                print(f"PARABÉNS! {player2_name} GANHOU O JOGO!")
                break
            
            current_player = 1
        
        input("\nPressione Enter para continuar...")
    
    print(f"\nTotal de turnos: {turn_count}")
    input("\nPressione Enter para voltar ao menu...")


if __name__ == "__main__":
    jogo_da_gloria()