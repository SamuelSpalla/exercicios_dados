tupla = (1, 2, 3, 4, 5)

cont_par = 0
cont_impar = 0


for i in range(len(tupla)):
    if tupla[i] % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f'Par: {cont_par}')
print(f'Impar: {cont_impar}')