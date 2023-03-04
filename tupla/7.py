tupla = ('Uva','Laranja', 'Kiwia', 'Abacaxi', 'Banana')

ver = input('Digite uma fruta para verificar:').capitalize()

cont = 0

for i in tupla:
    if i == ver:
        print('Essa fruta está na lista')
    else:
        cont += 1
        pass

if cont == len(tupla):
    print('Essa fruta não esta na lista')