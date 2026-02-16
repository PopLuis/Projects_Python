class Carte:
    def __init__(self, titlu, autor):
        self.titlu = titlu
        self.autor = autor
        self.disponibila=True

    def imprumuta(self):
        if self.disponibila:
            self.disponibila = False
            print("Cartea a fost imprumutata")
        else:
            print("Cartea nu este disponibila")

    def returneaza(self):
        if self.disponibila:
            self.disponibila=True
            print("Cartea a fost returnata")
        else:
            print("Cartea nu este inchiriata")


    def afiseaza(self):
        print(f"{self.titlu} - {self.autor} | Disponibila: {self.disponibila}")



class Bibliotaca:
    def __init__(self):
        self.lista_carti=[]

    def adauga_carte(self, carte):
        self.lista_carti.append(carte)

    def afiseaza_carti(self):
        for carte in self.lista_carti:
            carte.afiseaza()

    def imprumuta_carte(self, titlu):
        for carte in self.lista_carti:
            if carte.titlu == titlu:
                carte.imprumuta()
                return
        print("Cartea nu exista in biblioteca")


b = Bibliotaca()

c1 = Carte("Povesti", "Ion Creanga")
c2 = Carte("Python", "Popescu")

b.adauga_carte(c1)
b.adauga_carte(c2)

b.afiseaza_carti()

b.imprumuta_carte("Povesti")
b.afiseaza_carti()
