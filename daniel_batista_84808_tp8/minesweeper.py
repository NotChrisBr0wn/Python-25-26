import random
import os

def minesweeper(save=None):
    LINHAS, COLUNAS, BOMBAS = 5, 5, 3
    
    if save:
        tab_real = save['real']
        tab_visivel = save['visivel']
    else:
        tab_real = [["0" for _ in range(COLUNAS)] for _ in range(LINHAS)]
        bombas_colocadas = 0
        while bombas_colocadas < BOMBAS:
            l, c = random.randint(0, LINHAS-1), random.randint(0, COLUNAS-1)
            if tab_real[l][c] != "B":
                tab_real[l][c] = "B"
                bombas_colocadas += 1
        tab_visivel = [["?" for _ in range(COLUNAS)] for _ in range(LINHAS)]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== MINESWEEPER ===")
        print("   " + " ".join([str(i) for i in range(COLUNAS)]))
        for i, linha in enumerate(tab_visivel):
            print(f"{i} | {' '.join(linha)}")
        
        print("\n(S) Sair e Guardar | Coordenadas: L C")
        entrada = input("Escolha: ").strip().upper()

        if entrada == 'S': return {"real": tab_real, "visivel": tab_visivel}

        try:
            l, c = map(int, entrada.split())
            if tab_real[l][c] == "B":
                print("💥 BOOM! Perdeste.")
                input("Enter para sair...")
                return "derrota"
            else:
                tab_visivel[l][c] = " " # Abre a casa
                if sum(r.count("?") for r in tab_visivel) == BOMBAS:
                    print("🏆 VITÓRIA!")
                    return "vitoria"
        except: continue
        
if __name__ == "__main__":
    minesweeper()