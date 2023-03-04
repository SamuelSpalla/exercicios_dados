tupla = (1, 3, 5, 8, 10)

ver = int(input('Digite um número para verificar:'))

cont = 0

for i in tupla:
    if i == ver:
        print('Esse numero está na lista')
    else:
        cont += 1
        pass
    

if cont == len(tupla):
    print('Esse número não esta na lista')