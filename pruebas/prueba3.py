import random

acumulado = 0
cartas = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(cartas[0][0])
while True:
    while True:
        i = random.randint(0, 3)
        j = random.randint(0, 9)
        if cartas[i][j] != 0:
            break
    if cartas[i][j] > 7:
        carta = 0.5
    else:
        carta = cartas[i][j]
    print("Tu carta es", carta, '\n')
    acumulado += carta
    cartas[i][j] = 0
    print('Tienes acumulado: ', acumulado)
    if acumulado == 7.5:
        print("Has ganado!!")
    elif acumulado > 7.5:
        print("Te has pasado! Has perdido")
    else:
        respuesta = input("QUieres otra (S/N) ")
    if respuesta == 'n' or acumulado >= 7.5:
        break
for i in range(len(cartas)):
    print()
    for j in range(len(cartas[0])):
        print(cartas[i][j], end='\t')

