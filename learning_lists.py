## crearea listelor
numere = [1, 2, 3, 4, 5]
nume = ["Ana", "Ion", "Maria"]
mix = [1, "text", 3.5, True]

##Acesarea listelor
numere = [10, 20, 30, 40]

print(numere[0])   # 10
print(numere[2])   # 30
print(numere[-1])  # 40 (ultimul element)

##Modificare listelor
numere = [1, 2, 3]
numere[1] = 10
print(numere)

##Adaugare elem

lista = [1, 2]
lista.append(3)
lista.insert(1, 100)

##Stergerea elem
lista = [1, 2, 3, 4]

lista.remove(3)   # șterge valoarea
lista.pop()       # șterge ultimul
lista.pop(1)      # șterge de pe index
del lista[0]      # șterge prin index

##Parcurgerea listelor
lista = [1, 2, 3]

for x in lista:
    print(x)

for i in range(len(lista)):
    print(lista[i])

##Verificare 
if 3 in lista:
    print("Există")
