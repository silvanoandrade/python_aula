import random
import string

def gerar_senha_segura(tamanho):
    """
    Gera uma senha segura com letras maiúsculas, minúsculas, números e símbolos.
    Garantindo que a senha tenha pelo menos um de cada tipo.
    """
    if tamanho < 4:
        raise ValueError("O tamanho mínimo para uma senha segura é 4 caracteres.")

    # Listas de caracteres por tipo
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Garante pelo menos um de cada tipo
    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Preenche o restante da senha com caracteres aleatórios
    todos_caracteres = maiusculas + minusculas + numeros + simbolos
    senha += random.choices(todos_caracteres, k=tamanho-4)

    # Embaralha a senha para não ficar previsível
    random.shuffle(senha)

    return ''.join(senha)

# --- Programa principal ---
print("Bem-vindo ao gerador de senhas seguras!")

# Usuário define o tamanho da senha
tamanho = int(input("Digite o tamanho da senha que você deseja: "))

# Gera e mostra a senha
senha_gerada = gerar_senha_segura(tamanho)
print(f"Sua senha segura é: {senha_gerada}")