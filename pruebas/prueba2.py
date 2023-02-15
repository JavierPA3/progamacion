x = int(input('Introduzca un número: '))
y = int(input('Introduzca el segundo número: '))
z = int(input('Introduzca el tercer número: '))
if x < y:
    if x < z:
        menor = x
    else:
        menor = z
elif z < y:
    menor = z
else:
    menor = y
print('El menor es ', menor)
