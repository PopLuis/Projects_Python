def salut():
    print("Salut")

salut()
salut()
def salut_name(name):
    print("Salut " + name)
salut_name("Luis")

def suma(a,b):
    return a+b

print("Suma este: " + str(suma(3,6)))

def sal(nume="Ana"):
    print("Salut " + nume)

sal()
sal("Ioana")
def operatii(a, b):
    return a+b, a-b, a*b
s, d, p = operatii(10, 5)
print(s, d, p)

##numar variabil de elemente
def suma_totala(*numere):
    return sum(numere)

print(suma_totala(1, 2, 3, 4))
