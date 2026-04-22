import math


def is_prime(number: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é maior que 1 e possui apenas dois divisores positivos: 1 e ele mesmo.

    Args:
        number (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        ValueError: Se o número não for um inteiro positivo.
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("O número deve ser um inteiro não negativo.")

    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False

    # Calcula o limite até a raiz quadrada para otimizar a verificação
    limit = int(math.isqrt(number))
    # Verifica divisores ímpares de 3 até o limite
    for divisor in range(3, limit + 1, 2):
        if number % divisor == 0:
            return False
    return True


def get_user_input() -> int:
    """
    Solicita ao usuário um número inteiro.

    Returns:
        int: O número inserido pelo usuário.

    Raises:
        ValueError: Se a entrada não for um inteiro válido.
    """
    while True:
        try:
            user_input = input("Digite um número para verificar se é primo: ")
            return int(user_input)
        except ValueError:
            print("Por favor, insira um número inteiro válido.")


def display_result(number: int, is_prime_result: bool) -> None:
    """
    Exibe o resultado da verificação de primalidade.

    Args:
        number (int): O número verificado.
        is_prime_result (bool): True se primo, False caso contrário.
    """
    status = "é primo" if is_prime_result else "não é primo"
    print(f"{number} {status}.")


if __name__ == "__main__":
    try:
        num = get_user_input()
        result = is_prime(num)
        display_result(num, result)
    except ValueError as e:
        print(f"Erro: {e}")

