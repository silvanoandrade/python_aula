def calculadora():
    print("=== Calculadora Simples ===")

    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                print("Erro: divisão por zero!")
                return
            resultado = num1 / num2
        else:
            print("Operação inválida!")
            return

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Erro: digite apenas números válidos!")


if __name__ == "__main__":
    calculadora()