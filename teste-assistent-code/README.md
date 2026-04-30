# Projeto Teste Assistente de Código

Este projeto contém exercícios práticos de Python desenvolvidos para aprender conceitos fundamentais de programação, incluindo debug, números primos e refatoração de código.

## Estrutura do Projeto

```
teste-assistent-code/
├── debug.py              # Programa de nota fiscal com erros para debug
├── num-primos.py         # Verificação de números primos
├── refatoracao.py        # Cálculo de estatísticas
├── explicacao-debug.md   # Documentação dos erros em debug.py
├── explicacao-num-primo.md  # Explicação técnica de num-primos.py
└── explicacao-refatoracao.md # Explicação de refatoracao.py
```

## Arquivos

### 1. debug.py - Programa de Nota Fiscal

Um programa que calcula o total de uma compra com itens, imposto e desconto.

**Funcionalidades:**
- Entrada de dados do cliente e itens
- Cálculo de subtotal, imposto (10%) e desconto
- Exibição formatada de nota fiscal

**Como executar:**
```bash
python debug.py
```

> **Nota:** Este arquivo contém erros propositais para prática de debug. Veja [explicacao-debug.md](explicacao-debug.md) para os detalhes.

---

### 2. num-primos.py - Verificação de Números Primos

Programa que verifica se um número inteiro é primo.

**Funcionalidades:**
- Verificação eficiente usando raiz quadrada
- Validação de entrada
- Interface interativa

**Como executar:**
```bash
python num-primos.py
```

**Exemplo de uso:**
```python
from num-primos import is_prime

is_prime(17)  # Retorna True
is_prime(10)  # Retorna False
```

---

### 3. refatoracao.py - Cálculo de Estatísticas

Programa que calcula estatísticas básicas de uma lista de números.

**Funcionalidades:**
- Soma total
- Média aritmética
- Maior valor
- Menor valor

**Como executar:**
```bash
python refatoracao.py
```

**Exemplo de uso:**
```python
from refatoracao import calculate_statistics

numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, media, maximo, minimo = calculate_statistics(numeros)
```

---

## Documentação

Cada arquivo de código possui um arquivo de explicação correspondente:

| Código | Explicação |
|--------|------------|
| debug.py | [explicacao-debug.md](explicacao-debug.md) |
| num-primos.py | [explicacao-num-primo.md](explicacao-num-primo.md) |
| refatoracao.py | [explicacao-refatoracao.md](explicacao-refatoracao.md) |

---

## Conceitos Aprendidos

### Debug
- Identificação de erros de sintaxe
- Conversão de tipos (string para float)
- Uso correto de f-strings
- Comparação de tipos

### Números Primos
- Definição de número primo
- Otimização com raiz quadrada
- Validação de entrada
- Clean Code e documentação

### Refatoração
- Separação de responsabilidades
- Nomeação descritiva de variáveis
- Tratamento de erros
- Funções puras

---

## Requisitos

- Python 3.7 ou superior

## Autor

Projeto educacional desenvolvido para prática de programação Python.