# Explicação Técnica: Verificação de Número Primo em Python

## Introdução

Este documento explica tecnicamente o código implementado no arquivo `num-primos.py`, que verifica se um número inteiro é primo. Um número primo é um inteiro maior que 1 que possui apenas dois divisores positivos: 1 e ele mesmo. Por exemplo, 2, 3, 5, 7, 11 são primos, enquanto 4, 6, 8, 9 não são.

O código utiliza uma abordagem eficiente para determinar a primalidade, otimizada para reduzir o número de operações desnecessárias.

## Estrutura do Código

### Importações

```python
import math
```

- O módulo `math` é importado para utilizar a função `isqrt`, que calcula a raiz quadrada inteira de um número. Isso é usado para definir o limite superior da verificação de divisores.

### Função `is_prime(number: int) -> bool`

```python
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
```

#### Melhorias em Clean Code

- **Nomeação Clara**: Parâmetro renomeado de `n` para `number` para maior clareza.
- **Validação de Entrada**: Adicionada verificação de tipo e valor para garantir que apenas inteiros não negativos sejam aceitos, lançando `ValueError` se necessário.
- **Docstring Detalhada**: Inclui descrição, argumentos, retorno e exceções possíveis, seguindo convenções de documentação.
- **Comentários Inline**: Adicionados comentários explicativos para o cálculo do limite e o loop, melhorando a legibilidade sem afetar o desempenho.
- **Variáveis Descritivas**: `limite` renomeado para `limit`, e `i` para `divisor` para expressar melhor o propósito.

### Função `get_user_input() -> int`

```python
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
```

- **Separação de Responsabilidades**: Extraída do bloco principal para focar na obtenção de entrada, permitindo reutilização e teste independente.
- **Loop de Tentativa**: Garante que o usuário forneça uma entrada válida, melhorando a experiência do usuário.

### Função `display_result(number: int, is_prime_result: bool) -> None`

```python
def display_result(number: int, is_prime_result: bool) -> None:
    """
    Exibe o resultado da verificação de primalidade.

    Args:
        number (int): O número verificado.
        is_prime_result (bool): True se primo, False caso contrário.
    """
    status = "é primo" if is_prime_result else "não é primo"
    print(f"{number} {status}.")
```

- **Separação de Responsabilidades**: Foca exclusivamente na exibição do resultado.
- **Legibilidade**: Usa uma variável `status` para tornar o código mais claro.

### Bloco Principal

```python
if __name__ == "__main__":
    try:
        num = get_user_input()
        result = is_prime(num)
        display_result(num, result)
    except ValueError as e:
        print(f"Erro: {e}")
```

- **Estrutura Limpa**: O bloco principal agora é conciso, delegando tarefas para funções específicas.
- **Tratamento de Exceções**: Captura `ValueError` da função `is_prime` e exibe uma mensagem amigável.

## Análise de Complexidade

- **Tempo**: O(√n), pois o loop executa aproximadamente √n / 2 iterações no pior caso. Isso é muito eficiente para números grandes comparado a uma verificação linear até n.
- **Espaço**: O(1), pois usa apenas variáveis constantes, independente do tamanho de n.
- **Limitações**: Para números muito grandes (ex.: > 10^12), pode ser lento devido à natureza do algoritmo. Algoritmos probabilísticos como Miller-Rabin são mais eficientes para casos extremos.

## Exemplo de Execução

Suponha entrada: `7`

1. `n = 7`
2. `7 > 3` e `7 % 2 != 0`, então continua.
3. `limite = int(math.isqrt(7)) = 2`
4. Loop de 3 até 2: não executa.
5. Retorna `True`.
6. Imprime: "7 é primo."

Outro exemplo: `9`

1. `n = 9`
2. `9 > 3` e `9 % 2 != 0`.
3. `limite = 3`
4. Loop: `i=3`, `9 % 3 == 0`, retorna `False`.
5. Imprime: "9 não é primo."

## Melhorias Implementadas (Clean Code)

Esta versão do código foi refatorada seguindo princípios de Clean Code para aumentar a legibilidade, manutenibilidade e robustez:

- **Responsabilidades Separadas**: O código foi dividido em funções pequenas e focadas (`is_prime`, `get_user_input`, `display_result`), cada uma com uma única responsabilidade.
- **Validação Robusta**: Adicionada validação de entrada na função `is_prime` para prevenir erros inesperados.
- **Documentação Completa**: Docstrings detalhadas em todas as funções, explicando propósito, parâmetros, retorno e exceções.
- **Nomes Expressivos**: Variáveis e parâmetros renomeados para refletir seu significado (ex.: `n` → `number`, `limite` → `limit`, `i` → `divisor`).
- **Tratamento de Erros Melhorado**: Loop em `get_user_input` para insistir em entrada válida, e captura de exceções no bloco principal.
- **Comentários Inline**: Adicionados comentários explicativos sem sobrecarregar o código.
- **Consistência**: Uso uniforme de f-strings e estruturas de controle.

Essas mudanças tornam o código mais fácil de entender, testar e modificar, sem alterar a lógica ou eficiência algorítmica.

## Conclusão

Este código implementa uma verificação de primalidade eficiente e robusta, adequada para a maioria dos casos práticos. Ele demonstra boas práticas de programação em Python, como anotações de tipo, tratamento de exceções e otimização algorítmica. Para aplicações críticas ou números muito grandes, considere algoritmos mais avançados.
