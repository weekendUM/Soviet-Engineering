class Persoana(object):

    def __init__(self, nume):

       self.nume = nume

    def salut(self):

       print ("Salut")

class Profesor(Persoana):

    def __init__(self, nume, titlu):

       Persoana.__init__(self, nume)

       self.titlu = titlu

    def salut(self):

       print ("Buna ziua")

prof1 = Profesor("Decebal","Asistent")
Persoana.salut(prof1)