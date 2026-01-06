import random
import os
import time

def jogo_da_forca(save=None):
    BONECO = [
        """
           +---+
           |   |
               |
               |
               |
               |
         =========""", """
           +---+
           |   |
           O   |
               |
               |
               |
         =========""", """
           +---+
           |   |
           O   |
           |   |
               |
               |
         =========""", """
           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========""", """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
         =========""", """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
         =========""", """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
         ========="""
    ]

    if save:
        palavra_secreta = save['palavra']
        letras_adivinhadas = set(save['tentadas'])
        erros = save['erros']
        modo = save.get('modo', 'cpu')
    else:
        # --- ESCOLHA DE MODO (Alínea a) ---
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== JOGO DA FORCA ===")
        print("1. Contra Computador (Palavra Aleatória)")
        print("2. Contra Jogador 2 (Jogador 2 escolhe a palavra)")
        opcao = input("Escolha (1-2): ").strip()
        
        modo = '2p' if opcao == '2' else 'cpu'
        
        if modo == '2p':
            import getpass
            # getpass esconde a palavra enquanto é escrita
            palavra_secreta = getpass.getpass("Jogador 2, insira a palavra: ").strip().lower()
        else:
            diretorio_atual = os.path.dirname(__file__)
            caminho_ficheiro = os.path.join(diretorio_atual, "palavras.txt")
            try:
                with open(caminho_ficheiro, "r", encoding="utf-8") as f:
                    lista = [linha.strip().lower() for linha in f if linha.strip()]
                palavra_secreta = random.choice(lista)
            except:
                palavra_secreta = random.choice(["python", "arcade", "algoritmo"])
        
        letras_adivinhadas = set()
        erros = 0

    max_erros = 6

    def obter_visual():
        return " ".join([l if l in letras_adivinhadas else "_" for l in palavra_secreta])

    while erros < max_erros:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== FORCA ({'MODO 2P' if modo == '2p' else 'MODO CPU'}) ===")
        print(BONECO[erros])
        print(f"\nPalavra: {obter_visual()}")
        
        erradas = [l for l in letras_adivinhadas if l not in palavra_secreta]
        print(f"Letras erradas: {', '.join(sorted(erradas))}")
        print("-" * 25)
        print("(S) SALVAR E SAIR")
        
        entrada = input("Letra: ").strip().lower()

        if entrada == 's':
            return {
                "palavra": palavra_secreta,
                "tentadas": list(letras_adivinhadas),
                "erros": erros,
                "modo": modo
            }

        if len(entrada) != 1 or not entrada.isalpha():
            continue

        if entrada in letras_adivinhadas:
            print("⚠️ Já tentaste esta letra!"); time.sleep(0.5); continue

        letras_adivinhadas.add(entrada)

        if entrada not in palavra_secreta:
            erros += 1
        
        if all(l in letras_adivinhadas for l in palavra_secreta):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"🏆 VITÓRIA! A palavra era: {palavra_secreta.upper()}")
            input("\nPrime Enter...")
            return "vitoria_p1"

    os.system('cls' if os.name == 'nt' else 'clear')
    print(BONECO[6])
    print(f"💀 GAME OVER! A palavra era: {palavra_secreta.upper()}")
    input("\nPrime Enter...")
    # Se perder no modo 2P, o ponto vai para o Jogador 2. Se for CPU, vai para a CPU.
    return "vitoria_p2" if modo == '2p' else "vitoria_cpu"