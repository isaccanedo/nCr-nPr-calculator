import math
from typing import Tuple

def validar_entrada(n: int, r: int) -> Tuple[bool, str]:
    """
    Valida os valores de entrada n e r.
    
    Args:
        n: Número total de elementos
        r: Número de elementos a serem escolhidos
        
    Returns:
        Tuple contendo um booleano indicando se é válido e uma mensagem
    """
    if not isinstance(n, int) or not isinstance(r, int):
        return False, "Os valores devem ser números inteiros"
    if n < 0 or r < 0:
        return False, "Os valores não podem ser negativos"
    if r > n:
        return False, "O valor de r não pode ser maior que n"
    return True, ""

def combinacao(n: int, r: int) -> int:
    """
    Calcula a combinação de n elementos tomados r a r.
    
    Args:
        n: Número total de elementos
        r: Número de elementos a serem escolhidos
        
    Returns:
        Número de combinações possíveis
    """
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def permutacao(n: int, r: int) -> int:
    """
    Calcula a permutação de n elementos tomados r a r.
    
    Args:
        n: Número total de elementos
        r: Número de elementos a serem escolhidos
        
    Returns:
        Número de permutações possíveis
    """
    return math.factorial(n) // math.factorial(n - r)

def calcular_novamente() -> bool:
    """
    Pergunta ao usuário se deseja fazer novo cálculo.
    
    Returns:
        Boolean indicando se deve continuar
    """
    while True:
        resposta = input("\nDeseja fazer outro cálculo? (s/n): ").lower()
        if resposta in ['s', 'n']:
            return resposta == 's'
        print("Por favor, digite 's' para sim ou 'n' para não.")

def main():
    while True:
        print("\nAnálise de Combinações e Permutações")
        print("-" * 40)
        
        try:
            n = int(input("Digite o valor de n (total de elementos): "))
            r = int(input("Digite o valor de r (elementos a serem escolhidos): "))
            
            valido, mensagem = validar_entrada(n, r)
            if not valido:
                print(f"Erro: {mensagem}")
                if not calcular_novamente():
                    break
                continue
                
            comb = combinacao(n, r)
            perm = permutacao(n, r)

            print("\nResultados:")
            print("-" * 40)
            print(f"Combinação C({n},{r}) = {comb:,}")
            print(f"Permutação P({n},{r}) = {perm:,}")
            
            if not calcular_novamente():
                break
                
        except ValueError:
            print("Erro: Por favor digite apenas números inteiros")
            if not calcular_novamente():
                break
        except OverflowError:
            print("Erro: Os valores são muito grandes para calcular")
            if not calcular_novamente():
                break
    
    print("\nObrigado por usar o programa!")

if __name__ == "__main__":
    main()
