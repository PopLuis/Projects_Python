matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
##Dimensiunea

linii = len(matrice)
coloane = len(matrice[0])

print(linii, coloane)

# Parcurgerea
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        print(matrice[i][j], end=" ")
    print()

#Citirea unei matrici de la tastatura

n = int(input("Nr linii: "))
m = int(input("Nr coloane: "))

matrice = []

for i in range(n):
    linie = []
    for j in range(m):
        x = int(input())
        linie.append(x)
    matrice.append(linie)
