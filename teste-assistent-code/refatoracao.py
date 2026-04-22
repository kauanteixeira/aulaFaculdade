def calculate_statistics(numbers_list):
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numbers_list (list): Lista de números (int ou float).

    Returns:
        tuple: (soma_total, media, maior_valor, menor_valor)

    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numbers_list:
        raise ValueError("A lista não pode estar vazia.")

    total = sum(numbers_list)
    average = total / len(numbers_list)
    maximum = max(numbers_list)
    minimum = min(numbers_list)

    return total, average, maximum, minimum


# Exemplo de uso
sample_numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total_sum, average_value, max_value, min_value = calculate_statistics(sample_numbers)

print("Total:", total_sum)
print("Média:", average_value)
print("Maior:", max_value)
print("Menor:", min_value)