#1
dic = {'Nome': 'Samuel', 'Idade': 21, 'End': 'Itaipuaçu', 'Tel': 993893221}

#2
dic['Altura'] = 1.75

#3
dic.pop('Tel')

#4
dic['Idade'] = 22

#5
print(len(dic.items()))

#6 e 7
if 'Nome' in dic:
    print('Há o atributo nome no dicionário, com valor: ', dic['Nome'])

#8
for c in dic.keys():
    print(f'Chave: {c} // Valor: {dic[c]}')

#9

cont = {
        'Samuel': {
        'tel': '22222222',
        'end': 'Rua 1'
    },
        'Arthur': {
        'tel': '1111111111',
        "end": 'Rua 2'
    },
    'Felipe': {
        'tel': '333333333',
        'end': 'Rua 3'
    }
}

for c in cont.keys():
    print(f'Chave: {c} // Valor: {cont[c]}')





# 10

txt = 'Os dicionários Python são uma coleção que guarda valores multidimensionais para cada índice. Diferentemente de uma lista encadeada, que guarda apenas um valor por vez.' 
'Assim, é possível gerar estruturas mais complexas que simulam melhor a realidade e conseguem mapear instâncias do mundo real em um programa de software.'

palavras_cont = {'uma': 0, 'que': 0, 'Python': 0, 'JavaScript': 0}

for p in txt.split():
    if p in palavras_cont:
        palavras_cont[p] += 1

print(palavras_cont)



print(dic)