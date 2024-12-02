import math

def combinacao(n, r):
    """Calcula a combinação de n elementos tomados r a r."""
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def permutacao(n, r):
    """Calcula a permutação de n elementos tomados r a r."""
    return math.factorial(n) // math.factorial(n - r)

def main():
    print("Análise de Combinações e Permutações")
    
    while True:
        try:
            # Solicita os valores de n e r ao usuário
            n = int(input("\nDigite o valor de n (total de elementos): "))
            r = int(input("Digite o valor de r (elementos a serem escolhidos): "))

            if r > n:
                print("Erro: r não pode ser maior que n.")
                continue

            # Calcula combinações e permutações
            comb = combinacao(n, r)
            perm = permutacao(n, r)

            # Exibe os resultados
            print(f"\nCombinação de {n} elementos tomados {r} a {r}: C(n, r) = {comb}")
            print(f"Permutação de {n} elementos tomados {r} a {r}: P(n, r) = {perm}")
        except ValueError:
            print("Erro: Por favor, insira apenas números inteiros válidos.")
            continue

        # Pergunta ao usuário se deseja reiniciar ou sair
        reiniciar = input("\nDeseja calcular novamente? (s/n): ").strip().lower()
        if reiniciar != 's':
            print("\nSaindo do programa. Até logo!")
            break

# Executa o script
if __name__ == "__main__":
    main()
