def calculadora_imc():
    print("--- Calculadora de IMC: Saúde e Python ---")
    
    while True:
        print("\nMenu:")
        print("1: Calcular IMC")
        print("0: Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == '0':
            print("Encerrando o programa. Cuide-se!")
            break
        
        if escolha == '1':
            try:
                # Entrada de dados
                peso = float(input("Digite seu peso (kg): "))
                altura = float(input("Digite sua altura (m): "))

                if altura <= 0:
                    print("Erro: A altura deve ser maior que zero.")
                    continue

                # Cálculo do IMC
                imc = peso / (altura ** 2)
                
                print(f"\nSeu IMC é: {imc:.2f}")

                # Estrutura Condicional para Classificação
                if imc < 18.5:
                    classificacao = "Abaixo do peso"
                elif 18.5 <= imc < 25:
                    classificacao = "Peso normal"
                elif 25 <= imc < 30:
                    classificacao = "Sobrepeso"
                elif 30 <= imc < 35:
                    classificacao = "Obesidade Grau I"
                elif 35 <= imc < 40:
                    classificacao = "Obesidade Grau II"
                else:
                    classificacao = "Obesidade Grau III (Mórbida)"
                
                print(f"Classificação: {classificacao}")

            except ValueError:
                print("Erro: Por favor, use números (ex: 70.5 ou 1.75).")
        else:
            print("Opção inválida!")

# Execução
calculadora_imc()