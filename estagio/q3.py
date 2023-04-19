'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

import json

caminho = './dados.json'
with open(caminho, 'r') as file:
    temp = json.load(file)
valores = [x['valor'] for x in temp ]
resultado = min(valores)
print(resultado)
resultado = max(valores)
print(resultado)
dias =  sum([1 for x in temp if x['valor'] > sum(valores)/len(valores)])
print(dias)