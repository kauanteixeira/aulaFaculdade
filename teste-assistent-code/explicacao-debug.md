# Explicação dos Erros no Código debug.py

## Erros Identificados

1. **Linha 4: Falta de aspas na string do input**
   - Código: `item1 = float(input(Preço do item 1? ))`
   - Problema: A string "Preço do item 1? " não está entre aspas, causando um erro de sintaxe. Python não reconhece "Preço" como uma variável definida.

2. **Linha 13: Tipo incorreto para desconto_cupom**
   - Código: `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`
   - Problema: A função `input()` retorna uma string, mas o código tenta usar `desconto_cupom` como um número nas operações subsequentes (divisão e comparação).

3. **Linha 14: Operação com tipos incompatíveis**
   - Código: `desconto = subtotal * (desconto_cupom / 100)`
   - Problema: `desconto_cupom` é uma string, e não é possível dividir uma string por 100. Isso causará um TypeError.

4. **Linha 22: Falta do prefixo 'f' na f-string**
   - Código: `print(" Item 2:        R$ {total_item2:.2f}")`
   - Problema: Para usar interpolação de variáveis em strings, é necessário o prefixo 'f'. Sem ele, `{total_item2:.2f}` é tratado como texto literal.

5. **Linha 27: Comparação entre string e número**
   - Código: `if desconto_cupom > 0:`
   - Problema: `desconto_cupom` é uma string, e comparar uma string com um número pode levar a comportamentos inesperados ou erros. Em Python, strings são consideradas "maiores" que números, mas isso não é o comportamento desejado.

6. **Linha 28: Formatação de string como número**
   - Código: `print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")`
   - Problema: `desconto_cupom` é uma string, e o formato `.0f` é para números float. Isso causará um ValueError.

7. **Linha 31: Formatação redundante**
   - Código: `print(f" TOTAL:         R$ {round(total, 2):.2f}")`
   - Problema: `round(total, 2)` já arredonda para 2 casas decimais, e `.2f` formata novamente. Embora funcione, é redundante e pode ser simplificado para `{total:.2f}`.

## Correções Aplicadas

- Adicionei aspas à string do input na linha 4.
- Converti `desconto_cupom` para float após o input para permitir operações numéricas.
- Adicionei o prefixo 'f' à string na linha 22.
- Ajustei a comparação e formatação para usar o valor numérico de `desconto_cupom`.
- Simplifiquei a formatação do total final.
