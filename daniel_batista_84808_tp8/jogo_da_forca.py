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
        palavra = save['palavra']
        tentadas = set(save['tentadas'])
        erros = save['erros']
    else:
        # Podes carregar do teu palavras.txt aqui
        palavra = random.choice(["python", "arcade", "programacao"])
        tentadas = set()
        erros = 0

    while erros < 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        status = [l if l in tentadas else "_" for l in palavra]
        print(f"Palavra: {' '.join(status)}")
        print(f"Erros: {erros}/6 | Letras: {tentadas}")
        
        letra = input("\nLetra ou (S) para Sair: ").lower().strip()
        
        if letra == 's':
            return {"palavra": palavra, "tentadas": list(tentadas), "erros": erros}
        
        if len(letra) == 1 and letra.isalpha() and letra not in tentadas:
            tentadas.add(letra)
            if letra not in palavra: erros += 1
        
        if all(l in tentadas for l in palavra):
            print(f"🎉 Ganhaste! A palavra era {palavra}")
            return "vitoria"
    return "derrota"