import json
import os

def gerir_dados(modo="ler", dados=None):
    ficheiro = "arcade_data.json"
    if modo == "escrever":
        with open(ficheiro, "w") as f: json.dump(dados, f, indent=4)
    else:
        if os.path.exists(ficheiro):
            with open(ficheiro, "r") as f: return json.load(f)
        return {"p1": "", "p2": "", "scores": {"p1": 0, "p2": 0}, "saves": {}}

def menu():
    dados = gerir_dados()
    if not dados["p1"]:
        print("=== NOVA SESSÃO ===")
        dados["p1"] = input("Nome Jogador 1: ")
        dados["p2"] = input("Nome Jogador 2: ")
        gerir_dados("escrever", dados)

    while True:
        print(f"\nSESSÃO: {dados['p1']} ({dados['scores']['p1']}) vs {dados['p2']} ({dados['scores']['p2']})")
        print("1. Jogo do Galo\n2. 4 em Linha\n3. Minesweeper (NOVO)\n4. Sair")
        op = input("Escolha: ")

        # Lógica para carregar save ou novo jogo
        save_atual = dados["saves"].get(op)
        # Aqui chamarias: resultado = jogo_do_galo(save_atual)
        # Se resultado for um tabuleiro -> dados["saves"][op] = resultado (Guardar)
        # Se resultado for um vencedor -> dados["scores"][vencedor] += 1 (Pontuar)

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