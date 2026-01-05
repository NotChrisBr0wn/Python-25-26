import random
import os

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
    else:
        # Tentar abrir o ficheiro palavras.txt
        diretorio_atual = os.path.dirname(__file__)
        caminho_ficheiro = os.path.join(diretorio_atual, "palavras.txt")

        try:
            with open(caminho_ficheiro, "r", encoding="utf-8") as f:
                lista = [linha.strip().lower() for linha in f if linha.strip()]
            if not lista: raise FileNotFoundError
            palavra_secreta = random.choice(lista)
        except Exception:
            lista_emergencia = ["python", "arcade", "computador"]
            palavra_secreta = random.choice(lista_emergencia)
            print("⚠️ Ficheiro não lido. A usar lista padrão.")
        
        letras_adivinhadas = set()
        erros = 0

    max_erros = 6

    def obter_visual():
        return " ".join([l if l in letras_adivinhadas else "_" for l in palavra_secreta])

    while erros < max_erros:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== JOGO DA FORCA ===")
        print(BONECO[erros])
        print(f"\nPalavra: {obter_visual()}")
        
        erradas = [l for l in letras_adivinhadas if l not in palavra_secreta]
        print(f"Letras erradas: {', '.join(sorted(erradas))}")
        print("-" * 20)
        print("Digite uma letra ou 'S' para SALVAR e SAIR.")
        
        entrada = input("Escolha: ").strip().lower()

        if entrada == 's':
            return {
                "palavra": palavra_secreta,
                "tentadas": list(letras_adivinhadas),
                "erros": erros
            }

        # Validação
        if len(entrada) != 1 or not entrada.isalpha():
            print("❌ Inválido! Insira apenas uma letra.")
            input("Enter..."); continue

        if entrada in letras_adivinhadas:
            print(f"⚠️ Já tentaste a letra '{entrada}'.")
            input("Enter..."); continue

        letras_adivinhadas.add(entrada)

        if entrada not in palavra_secreta:
            erros += 1
            print(f"❌ A letra '{entrada}' não existe!")
            input("Enter...")
        
        # Verificar Vitória
        if all(l in letras_adivinhadas for l in palavra_secreta):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(BONECO[erros])
            print(f"\n🏆 VITÓRIA! A palavra era: {palavra_secreta.upper()}")
            input("\nVoltando ao menu...")
            return "vitoria_p1" 

    os.system('cls' if os.name == 'nt' else 'clear')
    print(BONECO[6])
    print(f"\n💀 PERDESTE! A palavra era: {palavra_secreta.upper()}")
    input("\nVoltando ao menu...")
    return "derrota"