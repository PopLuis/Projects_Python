class Produs:
    def __init__(self,nume,pret,stoc):
        self.nume=nume
        self.pret=pret
        self.stoc=stoc

    def afiseaza(self):
        print(f"Pordus: {self.nume} Pret: {self.pret} lei Stoc: {self.stoc} kg")

    def vinde(self, cantitate):
        if cantitate > self.stoc:
            print("Cantitatea este prea mare")
            return False
        else:
            self.stoc -= cantitate
            return True


class CosCumparaturi:
    def __init__(self):
        self.produse = []

    def adauga_prod(self,produs,cantitate):
        if produs.vinde(cantitate):
            self.produse.append((produs, cantitate))

    def total(self):
        tot = 0
        for produs, cantitate in self.produse:
            tot += produs.pret*cantitate
        return tot

    def afiseaza_cos(self):
        for produs, cantitate in self.produse:
            print(f"{produs.nume} x {cantitate} = {produs.pret * cantitate} lei")

pr1=Produs("Mar",12,20)
pr2=Produs("Para",3,222)

cos1 = CosCumparaturi()
cos1.adauga_prod(pr1,20)
cos1.adauga_prod(pr2,21)
cos1.afiseaza_cos()
print("Total: ", cos1.total())
