import os
import time
import random

RESET = "\033[0m"
COR_X = "\033[91m"  
COR_O = "\033[94m"  

PECA_X = f"{COR_X} X{RESET}"
PECA_O = f"{COR_O} O{RESET}"

def jogo_da_trilha(save=None):
    VIZINHOS = {
        0: [1, 9], 1: [0, 2, 4], 2: [1, 14], 3: [4, 10], 4: [1, 3, 5, 7], 
        5: [4, 13], 6: [7, 11], 7: [4, 6, 8], 8: [7, 12], 9: [0, 10, 21], 
        10: [3, 9, 11, 18], 11: [6, 10, 15], 12: [8, 13, 17], 13: [5, 12, 14, 20], 
        14: [2, 13, 23], 15: [11, 16], 16: [15, 17, 19], 17: [12, 16], 
        18: [10, 19], 19: [16, 18, 20, 22], 20: [13, 19], 21: [9, 22], 
        22: [19, 21, 23], 23: [14, 22]
    }

    if save:
        tab = save['tab']
        turno = save['turno']
        pecas_col = save['p_col']
        fase = save['fase']
        modo = save['modo']
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== JOGO DA TRILHA ===")
        print("1. Contra Computador\n2. Contra Jogador 2")
        modo = 'cpu' if input("Escolha: ") == '1' else '2p'
        tab = [f"{i:>2}" for i in range(24)]
        turno = PECA_X  
        pecas_col = {PECA_X: 9, PECA_O: 9} 
        fase = "COLOCAR"

    def mostrar_tabuleiro():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== TRILHA ({modo.upper()}) | TURNO:{turno} | FASE: {fase} ===")
        print(f"Pecas para colocar: X:{pecas_col[PECA_X]} | O:{pecas_col[PECA_O]}")
        print(f"""
        {tab[0]}-----------{tab[1]}-----------{tab[2]}
        |             |            |                    
        |   {tab[3]}-------{tab[4]}-------{tab[5]}   |
        |   |         |        |   |                    
        |   |   {tab[6]}---{tab[7]}---{tab[8]}   |   |
        |   |   |          |   |   |                       
       {tab[9]}---{tab[10]}--{tab[11]}        {tab[12]}--{tab[13]}--{tab[14]}
        |   |   |          |   |   |                       
        |   |   {tab[15]}---{tab[16]}---{tab[17]}   |   |
        |   |         |        |   |                       
        |   {tab[18]}-------{tab[19]}-------{tab[20]}   |
        |             |            |                       
        {tab[21]}-----------{tab[22]}-----------{tab[23]}
        """)
        print("(S) SALVAR E SAIR")


    

    while True:
        mostrar_tabuleiro()
        
        # Lógica da CPU
        if modo == 'cpu' and turno == PECA_O:
            time.sleep(1)
            disponiveis = [i for i, v in enumerate(tab) if v not in [PECA_X, PECA_O]]
            
            if fase == "COLOCAR" and disponiveis: 
                pos = random.choice(disponiveis)
                tab[pos] = PECA_O
                pecas_col[PECA_O] -= 1
                
                if pecas_col[PECA_X] == 0 and pecas_col[PECA_O] == 0:
                    fase = "MOVER"     
            else:
                pass
        else:
            jogada = input(f"Jogador{turno}, escolha posição: ").strip().upper()
            if jogada == 'S' or jogada == 's':
                return {"tab": tab, "turno": turno, "p_col": pecas_col, "fase": fase, "modo": modo}
            
            try:
                if fase == "COLOCAR":
                    pos = int(jogada)
                    if tab[pos] not in [PECA_X, PECA_O]:
                        tab[pos] = turno
                        pecas_col[turno] -= 1
                        if pecas_col[PECA_X] == 0 and pecas_col[PECA_O] == 0:
                            fase = "MOVER"
                    else:
                        print("❌ Ocupado!"); time.sleep(1); continue
                
                elif fase == "MOVER":
                    # Mover peça como na batalha naval ex: 0 1
                    print("Exemplo: '0 1' para mover da casa 0 para a 1")
                    origem, destino = map(int, jogada.split())
                    if tab[origem] == turno and tab[destino] not in [PECA_X, PECA_O]:
                        if destino in VIZINHOS[origem]:
                            tab[origem] = f"{origem:>2}"
                            tab[destino] = turno
                        else:
                            print("❌ Movimento inválido!"); time.sleep(1); continue
                    else:
                        print("❌ Peça errada ou destino ocupado!"); time.sleep(1); continue
            except:
                print("❌ Entrada inválida!"); time.sleep(1); continue

        # Vitoria
        if fase == "MOVER":
            count_x = tab.count(PECA_X)
            count_o = tab.count(PECA_O)
            if count_x < 3: return "vitoria_p2"
            if count_o < 3: return "vitoria_p1" if modo == '2p' else "vitoria_cpu"
        
        # Troca turno
        turno = PECA_O if turno == PECA_X else PECA_X