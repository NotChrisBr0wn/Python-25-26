import random
import os

def minesweeper(save=None):
    L, C, BOMBAS = 5, 5, 3
    if save:
        real, visivel = save['real'], save['visivel']
    else:
        real = [["0" for _ in range(C)] for _ in range(L)]
        for _ in range(BOMBAS):
            while True:
                rl, rc = random.randint(0, L-1), random.randint(0, C-1)
                if real[rl][rc] != "B":
                    real[rl][rc] = "B"; break
        visivel = [["?" for _ in range(C)] for _ in range(L)]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("   " + " ".join(str(i) for i in range(C)))
        for i, row in enumerate(visivel):
            print(f"{i} | {' '.join(row)}")
        
        escolha = input("\nCoordenadas (L C) ou (S) Sair: ").strip().upper()
        if escolha == 'S': return {"real": real, "visivel": visivel}

        try:
            l, c = map(int, escolha.split())
            if real[l][c] == "B":
                print("💥 BOOM! Acertaste numa mina.")
                input("Enter..."); return "derrota"
            visivel[l][c] = "." 
            if sum(r.count("?") for r in visivel) == BOMBAS:
                print("🏆 Campo Limpo!"); input("Enter..."); return "vitoria"
        except: continue