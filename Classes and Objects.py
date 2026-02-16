class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades

    def afiseare(self):
        print(self.name, self.age, self.grades)


s1=Student("Mihai",10,10)
s2=Student("Ion",10,9)
s3=Student("Luis",10,8)
s1.afiseare()
s2.afiseare()
s3.afiseare()


class Dreptunghi():
    def __init__(self,L,l):
        self.L=L
        self.l=l


    def Aria(self):
        print(self.l*self.L)

    def Perimetrul(self):
        print(self.L+self.l)


Drept1=Dreptunghi(10,2)
Drept1.Aria()
Drept1.Perimetrul()


class ContBancar:
    def __init__(self,sold):
        self.sold=sold

    def Depunere(self,suma):
        self.sold+=suma
    def Retragere(self,suma):
        self.sold-=suma

    def af_sold(self):
        print(f"Soldul este: {self.sold}")


cont1=ContBancar(1000)
cont1.Depunere(1000)
cont1.af_sold()
cont1.Retragere(500)
cont1.af_sold()

class Catalog:
    def __init__(self,nume,lista_note):
        self.nume = nume
        self.lista_note=lista_note


    def Medie(self):
        return sum(self.lista_note)/len(self.lista_note)

    def afisare(self):
        print(f"nume: {self.nume}")
        print(f"note: {self.lista_note}")
        print(f"Medie: {self.Medie()}")

elev1=Catalog("Luis",[10,3,4])
elev2=Catalog("Mihai",[2,9,10])

elev2.afisare()
elev1.afisare()
