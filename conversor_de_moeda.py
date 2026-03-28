def converter():
    taxa = 6.0

    while True:
        print("\nConversor de Moeda 💱")
        print("1 - Euro para Real")
        print("2 - Real para Euro")

        opcao = input("Escolha a opção (1 ou 2): ")

        if opcao == "1":
            euros = float(input("Digite o valor em euros: €"))
            reais = euros * taxa
            print(f"€{euros:.2f} = R${reais:.2f}")

        elif opcao == "2":
            reais = float(input("Digite o valor em reais: R$"))
            euros = reais / taxa
            print(f"R${reais:.2f} = €{euros:.2f}")

        else:
            print("Opção inválida!")

        # 👇 agora roda sempre
        continuar = input("\nDeseja continuar? (s/n): ").lower()

        if continuar != "s":
            print("Encerrando... 👋")
            break

converter()

