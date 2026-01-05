import json
import os

def gerir_dados(modo="ler", dados=None):
    """Lida com a leitura e escrita no ficheiro JSON para persistência"""
    ficheiro = "arcade_data.json"
    if modo == "escrever":
        with open(ficheiro, "w", encoding="utf-8") as f: 
            json.dump(dados, f, indent=4)
    else:
        # Verifica se o ficheiro existe e não está vazio
        if os.path.exists(ficheiro) and os.path.getsize(ficheiro) > 0:
            with open(ficheiro, "r", encoding="utf-8") as f: 
                return json.load(f)
        # Estrutura padrão para nova sessão
        return {"p1": "", "p2": "", "scores": {"p1": 0, "p2": 0}, "saves": {}}

GAMES = [
    ("Jogo do Galo", "jogo_do_galo", "jogo_do_galo"),
    ("4 em Linha", "quatro_em_linha", "quatro_em_linha"),
    ("Jogo da Glória", "jogo_da_gloria", "jogo_da_gloria"),
    ("Jogo da Forca", "jogo_da_forca", "jogo_da_forca"),
    ("Minesweeper", "minesweeper", "minesweeper"), # Corrigido para o nome da função no seu ficheiro
]

def import_and_run(module_name, func_name, save_data):
    """Importa o módulo e executa a função passando o parâmetro save"""
    try:
        modulo = __import__(module_name)
        func = getattr(modulo, func_name)
        # Executa o jogo passando o save (que pode ser None)
        return func(save=save_data)
    except Exception as e:
        print(f"Erro ao carregar o jogo {module_name}: {e}")
        return None

def menu():
    dados = gerir_dados()
    
    # Pergunta se deseja continuar a sessão anterior
    if dados["p1"]:
        print(f"\nSessão encontrada: {dados['p1']} vs {dados['p2']}")
        resp = input("Deseja continuar esta sessão? (s/n): ").lower()
        if resp != 's':
            dados = {"p1": "", "p2": "", "scores": {"p1": 0, "p2": 0}, "saves": {}}

    # Configuração de nomes para nova sessão
    if not dados["p1"]:
        print("\n=== NOVA SESSÃO ===")
        dados["p1"] = input("Nome Jogador 1: ") or "Jogador 1"
        dados["p2"] = input("Nome Jogador 2: ") or "Jogador 2"
        gerir_dados("escrever", dados)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== ARCADE CENTER ===")
        print(f"SESSÃO: {dados['p1']} ({dados['scores']['p1']}) vs {dados['p2']} ({dados['scores']['p2']})")
        print("-" * 30)
        
        for i, (name, _, _) in enumerate(GAMES, start=1):
            status = "[CONTINUAR]" if str(i) in dados["saves"] else "[NOVO]"
            print(f"{i}. {name} {status}")
        
        print(f"{len(GAMES) + 1}. Sair")
        
        escolha = input(f"\nEscolha (1-{len(GAMES) + 1}): ").strip()

        if escolha.isdigit():
            n = int(escolha)
            if 1 <= n <= len(GAMES):
                nome_jogo, mod_name, func_name = GAMES[n - 1]
                
                # Recupera o save se existir
                save_atual = dados["saves"].get(escolha)
                
                # Executa o jogo
                resultado = import_and_run(mod_name, func_name, save_atual)

                # Processa o que o jogo devolveu
                if isinstance(resultado, dict):
                    # O jogador saiu com 'S', guarda o estado
                    dados["saves"][escolha] = resultado
                    print("\nJogo guardado!")
                elif resultado:
                    # O jogo terminou (vitoria ou derrota), remove o save
                    if escolha in dados["saves"]:
                        del dados["saves"][escolha]
                    
                    # Atribui pontos
                    if "vitoria_p1" in str(resultado) or "vitoria_X" in str(resultado):
                        dados["scores"]["p1"] += 1
                    elif "vitoria_p2" in str(resultado) or "vitoria_O" in str(resultado):
                        dados["scores"]["p2"] += 1
                    elif resultado == "vitoria": 
                        dados["scores"]["p1"] += 1
                
                gerir_dados("escrever", dados)
                input("\nPrime Enter para voltar...")
                
            elif n == len(GAMES) + 1:
                break

if __name__ == "__main__":
    menu()