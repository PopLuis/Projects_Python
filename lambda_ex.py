def patrat(x):
    return x * x

print(patrat(4))   # 16

#lambda

patrat = lambda x: x * x

print(patrat(4))   # 16

suma = lambda a, b: a + b

print(suma(3, 5))   # 8

numere = [1, 2, 3, 4]

patrate = list(map(lambda x: x * x, numere))

print(patrate)

numere = [1, 2, 3, 4, 5, 6]

pare = list(filter(lambda x: x % 2 == 0, numere))

print(pare)

elevi = [("Ana", 9), ("Ion", 7), ("Maria", 10)]

ordonati = sorted(elevi, key=lambda x: x[1])

print(ordonati)

valori = [-3, -1, 2, 5]

rez = list(map(lambda x: x if x > 0 else 0, valori))

print(rez)
