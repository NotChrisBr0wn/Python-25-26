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

    # Carregar palavras do ficheiro txt
    try:
        with open("palavras.txt", "r", encoding="utf-8") as f:
            palavras = [linha.strip().lower() for linha in f if linha.strip()]
    except FileNotFoundError:
        # Usa uma lista padrão se o ficheiro não existir
        palavras = ["python", "programacao", "desenvolvedor", "computador"]
        print("⚠️ Ficheiro 'palavras.txt' não encontrado. A usar uma lista padrão...")

    palavra_secreta = random.choice(palavras)
    letras_adivinhadas = set()
    erros = 0
    max_erros = 6
    
    # Mostra a palavra com letras adivinhadas
    def mostrar_palavra():
        return ' '.join([letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta])

    print("\n" + "="*30)
    print("  BEM-VINDO AO JOGO DA FORCA")
    print("="*30)

    while erros < max_erros:
        print(BONECO[erros]) # Mostra o boneco atualizado
        print(f"\nPalavra: {mostrar_palavra()}")
        print(f"Letras usadas: {', '.join(sorted(letras_adivinhadas))}")
        
        palpite = input("\nAdivinhe uma letra: ").strip().lower()

        # Validações
        if len(palpite) != 1 or not palpite.isalpha(): # Verifica se o palpite é uma única letra
            print("⚠️ Por favor, insira apenas uma letra.")
            continue

        if palpite in letras_adivinhadas: # Verifica se a letra já foi adivinhada
            print(f"⚠️ Já tentaste a letra '{palpite}'. Tenta outra.")
            continue

        letras_adivinhadas.add(palpite)

        if palpite in palavra_secreta:
            print(f"✅ Boa! A letra '{palpite}' existe na palavra.")
        else:
            erros += 1
            print(f"❌ Errado! A letra '{palpite}' não existe. (Tentativas restantes: {max_erros - erros})")

        # Verifica se ganhou
        if all(letra in letras_adivinhadas for letra in palavra_secreta):
            print(f"\n🎉 PARABÉNS! A palavra era '{palavra_secreta.upper()}'.")
            print("Ganhaste o jogo!")
            break
    else:
        print(BONECO[max_erros])
        print(f"\n💀 FIM DE JOGO! Enforcastes-te. A palavra era '{palavra_secreta.upper()}'.")

if __name__ == "__main__":
    jogo_da_forca()