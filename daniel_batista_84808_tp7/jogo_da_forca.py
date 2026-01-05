import random
import os

def jogo_da_forca():
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

    diretorio_atual = os.path.dirname(__file__)
    caminho_ficheiro = os.path.join(diretorio_atual, "palavras.txt")

    try:
        with open(caminho_ficheiro, "r", encoding="utf-8") as f:
            lista_palavras = [linha.strip().lower() for linha in f if linha.strip()]
        
        if not lista_palavras:
            raise FileNotFoundError
        
        palavra_secreta = random.choice(lista_palavras)
    except Exception:
        lista_seguranca = ["python", "programacao", "computador", "algoritmo"]
        palavra_secreta = random.choice(lista_seguranca)
        print("⚠️ Aviso: 'palavras.txt' não encontrado. A usar lista de emergência.")
        input("Prime Enter para jogar...")

    letras_adivinhadas = set()
    erros = 0
    max_erros = 6

    def mostrar_palavra():
        return " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra_secreta])
    
    # --- Main Loop ---
    while erros < max_erros:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=== JOGO DA FORCA ===")
        print(BONECO[erros])
        print(f"\nPalavra: {mostrar_palavra()}")
        
        erradas = [l for l in letras_adivinhadas if l not in palavra_secreta]
        print(f"Letras erradas: {', '.join(sorted(erradas))}")
        print(f"Tentativas restantes: {max_erros - erros}")

        palpite = input("\nEscolha uma letra: ").strip().lower()

        if len(palpite) != 1 or not palpite.isalpha():
            print("❌ Erro: Insira apenas uma letra!")
            input("Enter...")
            continue

        if palpite in letras_adivinhadas:
            print(f"⚠️ Já tentaste a letra '{palpite}'.")
            input("Enter...")
            continue

        letras_adivinhadas.add(palpite)

        if palpite in palavra_secreta:
            print(f"✅ Boa! A letra '{palpite}' existe.")
        else:
            erros += 1
            print(f"❌ Errado! A letra '{palpite}' não existe.")
        
        if all(letra in letras_adivinhadas for letra in palavra_secreta):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"🏆 PARABÉNS! Ganhaste! A palavra era: {palavra_secreta.upper()}")
            input("\nPrime Enter para voltar ao menu...")
            return "vitoria"

    os.system('cls' if os.name == 'nt' else 'clear')
    print(BONECO[6])
    print(f"\n💀 PERDESTE! O boneco foi enforcado.")
    print(f"A palavra correta era: {palavra_secreta.upper()}")
    input("\nPrime Enter para continuar...")
    return "derrota"

if __name__ == "__main__":
    jogo_da_forca()