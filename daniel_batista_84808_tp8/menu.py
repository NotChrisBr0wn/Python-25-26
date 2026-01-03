import json
import os

def guardar_dados(dados):
    """Guarda o dicionário de dados no ficheiro JSON"""
    with open("arcade_data.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

def carregar_dados():
    """Carrega os dados do ficheiro. Se não existir, cria uma estrutura nova."""
    if os.path.exists("arcade_data.json"):
        with open("arcade_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "sessao_ativa": False,
        "jogadores": {"p1": "", "p2": ""},
        "pontuacao": {"p1": 0, "p2": 0},
        "saves": {} # Aqui guardamos o tabuleiro de cada jogo
    }

# Exemplo de lógica para o início do menu.py
def carregar_sessao():
    if os.path.exists("sessao.json"):
        quer_continuar = input("Deseja continuar a sessão anterior? (s/n): ").lower()
        if quer_continuar == 's':
            # código para ler o ficheiro e carregar nomes/pontuações
            pass

GAMES = [
    ("Jogo do Galo", "jogo_do_galo", "jogo_do_galo"),
    ("4 em Linha", "quatro_em_linha", "quatro_em_linha"),
    ("Jogo da Glória", "jogo_da_gloria", "jogo_da_gloria"),
    ("Jogo da Forca", "jogo_da_forca", "jogo_da_forca"),
    ("Minesweeper", "minesweeper", "main_minesweeper"),
]


def import_and_run(module_name: str, func_name: str):
    # Try absolute import first, then local import fallback
    try:
        module = __import__(f"daniel_batista_84808_tp6.{module_name}", fromlist=[func_name])
        func = getattr(module, func_name)
    except Exception:
        try:
            module = __import__(module_name)
            func = getattr(module, func_name)
        except Exception as e:
            print(f"Não foi possível importar {module_name}: {e}")
            return

    try:
        func()
    except Exception as e:
        print(f"Ocorreu um erro ao executar o jogo: {e}")


def menu():
    while True:
        print("\nBem vindo ao Arcade Center!")
        for i, (name, _, _) in enumerate(GAMES, start=1):
            print(f"{i}. {name}")
        print(f"{len(GAMES) + 1}. Sair")
        choice = input(f"Por favor selecione uma das opções (1-{len(GAMES) + 1}): ").strip()

        if choice.isdigit():
            n = int(choice)
            if 1 <= n <= len(GAMES):
                _, module_name, func_name = GAMES[n - 1]
                import_and_run(module_name, func_name)
            elif n == len(GAMES) + 1:
                print("Obrigado pela visita! Até a próxima.")
                break
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nSaindo...")