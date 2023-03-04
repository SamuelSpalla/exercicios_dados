tupla = (1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8)

tupla = tuple(filter((6).__ne__, tupla))

print(tupla)