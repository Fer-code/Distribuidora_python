import json

with open('dados.json', encoding='utf-8') as fatura_json:
    dados = json.load(fatura_json)

lista_valores = []

for i in dados:
    v = i['valor']
    
    if v != 0:
        lista_valores.append(v)

#-----------------------------------------
def media_valores(lista):
    media = sum(lista) / len(lista)
    return media

#-----------------------------------------
def superior_media(lista):

    lista_superior = []
    for v in lista:
        if v > media_valores(lista):
            lista_superior.append(v)

    quant_dias = len(lista_superior)
    return quant_dias


#-----------------------------------------
#print(media_valores(lista_valores))

print("\n  O menor valor de faturamento ocorrido em um dia do mês {}".format(min(lista_valores)))
print("\n  O maior valor de faturamento ocorrido em um dia do mês {}".format(max(lista_valores)))
print("\n  O número de dias em que o faturamento foi maior que a média é {}".format(superior_media(lista_valores)))



