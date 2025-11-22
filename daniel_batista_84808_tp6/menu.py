def menu():
    while True:
        print("Bem vindo ao Arcade Center!")
        print("1. Jogo do Galo")
        print("2. 4 em Linha")
        print("3. Jogo da Gloria")
        print("4. Sair")
        choice = input("Por favor selecione uma das opções (1-4): ")

        if choice == '1':
            from daniel_batista_84808_tp6.jogo_do_galo import jogo_do_galo
            jogo_do_galo()
        elif choice == '2':
            from daniel_batista_84808_tp6.quatro_em_linha import quatro_em_linha
            quatro_em_linha()
        elif choice == '3':
            from daniel_batista_84808_tp6.jogo_da_gloria import jogo_da_gloria
            jogo_da_gloria()
        elif choice == '4':
            print("Obrigado pela visita! Até a próxima.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()