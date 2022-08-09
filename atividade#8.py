#criando uma matriz e somando seus valores, todas as colunas e linhas individualmente.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sl1= sl2= sl3= sc1= sc2= sc3= 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' *30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end = "")
    print()
print('-=' * 30)
for l in range(0, 3):
    sc1 += matriz[l][0]
    sc2 += matriz[l][1]
    sc3 += matriz[l][2]
print(f'A soma dos valores da primeira coluna é {sc1}')
print(f'A soma dos valores da segunda coluna é {sc2}')
print(f'A soma dos valores da terceira coluna é {sc3}')
print('-=' * 30)
for c in range(0, 3):
    sl1 += matriz[0][c]
    sl2 += matriz[1][c]
    sl3 += matriz[2][c]
print(f'A soma dos valores da primeira linha é {sl1}')
print(f'A soma dos valores da segunda linha é {sl2}')
print(f'A soma dos valores da terceira linha é {sl3}')