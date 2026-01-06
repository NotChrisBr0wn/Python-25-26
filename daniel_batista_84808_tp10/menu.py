import json
import os
import time

def gerir_dados(modo="ler", dados=None):
    diretorio_local = os.path.dirname(os.path.abspath(__file__))
    ficheiro_arcade = os.path.join(diretorio_local, "arcade_data.json")
    ficheiro_idiomas = os.path.join(diretorio_local, "languages.json")
    
    if modo == "idiomas":
        try:
            if os.path.exists(ficheiro_idiomas):
                with open(ficheiro_idiomas, "r", encoding="utf-8") as f:
                    return json.load(f)
            else:
                return {
                    "pt": {"arcade_title": "=== ARCADE ===", "points": "Pontos: {}: {} | {}: {} | CPU: {}", "choice": "Escolha: ", "exit": "Sair", "continue": "[C]", "new": "[N]", "back": "Enter para voltar", "continue_session": "Continuar sessão? ", "new_session": "Nova Sessão", "p1_name": "Nome P1: ", "p2_name": "Nome P2: "},
                    "en": {"arcade_title": "=== ARCADE ===", "points": "Points: {}: {} | {}: {} | CPU: {}", "choice": "Choice: ", "exit": "Exit", "continue": "[C]", "new": "[N]", "back": "Enter to back", "continue_session": "Continue session? ", "new_session": "New Session", "p1_name": "P1 Name: ", "p2_name": "P2 Name: "}
                }
        except: return None

    if modo == "escrever":
        with open(ficheiro_arcade, "w", encoding="utf-8") as f: 
            json.dump(dados, f, indent=4)
    else:
        if os.path.exists(ficheiro_arcade) and os.path.getsize(ficheiro_arcade) > 0:
            try:
                with open(ficheiro_arcade, "r", encoding="utf-8") as f: 
                    d = json.load(f)
                    if "scores" not in d: d["scores"] = {"p1": 0, "p2": 0, "cpu": 0}
                    return d
            except: pass
        return {"p1": "", "p2": "", "scores": {"p1": 0, "p2": 0, "cpu": 0}, "saves": {}, "lang": "pt"}

GAMES = [
    ("Jogo do Galo", "jogo_do_galo", "jogo_do_galo"),
    ("4 em Linha", "quatro_em_linha", "quatro_em_linha"),
    ("Jogo da Glória", "jogo_da_gloria", "jogo_da_gloria"),
    ("Jogo da Forca", "jogo_da_forca", "jogo_da_forca"),
    ("Minesweeper", "minesweeper", "minesweeper"),
    ("Batalha Naval", "batalha_naval", "batalha_naval"),
    ("Jogo do Moinho", "jogo_da_trilha", "jogo_da_trilha"),
]

def import_and_run(module_name, func_name, save_data):
    try:
        modulo = __import__(module_name)
        func = getattr(modulo, func_name)
        return func(save=save_data)
    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(2)
        return None

def menu():
    all_texts = gerir_dados(modo="idiomas")
    dados = gerir_dados()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. English / 2. Português")
    l_choice = input(">> ").strip()
    lang = "en" if l_choice == "1" else "pt"
    t = all_texts[lang]

    if dados.get("p1"):
        os.system('cls' if os.name == 'nt' else 'clear')
        resp = input(t["continue_session"].format(dados['p1'], dados['p2'])).lower()
        if resp not in ['s', 'y', 'sim', 'yes']:
            dados = {"p1": "", "p2": "", "scores": {"p1": 0, "p2": 0, "cpu": 0}, "saves": {}, "lang": lang}

    if not dados.get("p1"):
        print(t["new_session"])
        dados["p1"] = input(t["p1_name"]) or "P1"
        dados["p2"] = input(t["p2_name"]) or "P2"
        gerir_dados("escrever", dados)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(t["arcade_title"])
        sc = dados.get("scores", {"p1":0, "p2":0, "cpu":0})
        print(t["points"].format(dados['p1'], sc['p1'], dados['p2'], sc['p2'], sc['cpu']))
        print("-" * 40)
        
        for i, (name, _, _) in enumerate(GAMES, start=1):
            status = t["continue"] if str(i) in dados["saves"] else t["new"]
            print(f"{i}. {name} {status}")
        
        print(f"{len(GAMES) + 1}. {t['exit']}")
        
        escolha = input(t["choice"].format(len(GAMES) + 1)).strip()

        if escolha == str(len(GAMES) + 1): break
        
        if escolha in [str(i) for i in range(1, len(GAMES)+1)]:
            idx = int(escolha) - 1
            res = import_and_run(GAMES[idx][1], GAMES[idx][2], dados["saves"].get(escolha))
            
            if isinstance(res, dict):
                dados["saves"][escolha] = res
            elif res:
                if escolha in dados["saves"]: del dados["saves"][escolha]
                if "vitoria_p1" in str(res): dados["scores"]["p1"] += 1
                elif "vitoria_p2" in str(res): dados["scores"]["p2"] += 1
                elif "vitoria_cpu" in str(res): dados["scores"]["cpu"] += 1
            
            gerir_dados("escrever", dados)
            input(t["back"])

if __name__ == "__main__":
    menu()