import os

def jogo_do_galo(save=None):
    
    if save:
        tabuleiro = save
        x_count = tabuleiro.count('X')
        o_count = tabuleiro.count('O')
        simbolo_atual = 'X' if x_count <= o_count else 'O'
        p1_simbolo = 'X' 
    else:
        tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        # Escolher X ou O para o Jogador 1 
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== CONFIGURAÇÃO DO JOGO ===")
            escolha = input("Jogador 1, queres ser 'X' ou 'O'? ").strip().upper()
            if escolha in ['X', 'O']:
                p1_simbolo = escolha
                break
            print("⚠️ Escolha inválida!")
            input("Prime Enter...")
        simbolo_atual = p1_simbolo

    p2_simbolo = 'O' if p1_simbolo == 'X' else 'X'

    def mostrar_tabuleiro():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== JOGO DO GALO ===")
        print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
        print("---+---+---")
        print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
        print("---+---+---")
        print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n")
        print(f"Vez de: {simbolo_atual}")
        print("---------------------------")
        print("Digite 'S' para SALVAR e SAIR.")
        print("---------------------------")

    def verificar_vitoria(s):
        v = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == s for a,b,c in v)

    num_jogadas = sum(1 for x in tabuleiro if x in ['X', 'O'])

    while True:
        mostrar_tabuleiro()
        jogada = input("Escolha (1-9): ").strip().upper()

        # Guardar/Sair
        if jogada == 'S':
            print("\n💾 Status guardado. A voltar ao menu...")
            input("Prime Enter...")
            return tabuleiro 

        try:
            pos = int(jogada) - 1
            if 0 <= pos <= 8 and tabuleiro[pos] not in ['X', 'O']:
                tabuleiro[pos] = simbolo_atual
                num_jogadas += 1
            else:
                print("❌ Posição ocupada ou inválida!")
                input("Prime Enter...")
                continue
        except ValueError:
            print("❌ Opção inválida!")
            input("Prime Enter...")
            continue

        # Verificar vitória ou empate
        if verificar_vitoria(simbolo_atual):
            mostrar_tabuleiro()
            print(f"🏆 FIM DE JOGO! O símbolo {simbolo_atual} venceu!")
            input("\nPrime Enter para continuar...")
            return f"vitoria_{simbolo_atual}"

        if num_jogadas == 9:
            mostrar_tabuleiro()
            print("🤝 Empate! O tabuleiro ficou cheio.")
            input("\nPrime Enter para continuar...")
            return "empate"

        simbolo_atual = p2_simbolo if simbolo_atual == p1_simbolo else p1_simbolo

if __name__ == "__main__":
    jogo_do_galo()