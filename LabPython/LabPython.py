class Planta():
    def __init__(self, nume, clima, info):
        self.nume = nume
        self.clima = clima
        self.info = info
    def __str__(self):
        rez = "clima: " + self.clima + "\nnume: " + self.nume + "\ninfo:" + self.info
        return rez
    
    def __repr__(self):
        rez = "clima: " + self.clima + "\nnume: " + self.nume + "\ninfo:" + self.info
        return rez
    
class Trandafir(Planta):
    def __init__(self, clima, info, culoare, inaltime):
        super().__init__("trandafir", clima, info)
        self.culoare = culoare
        self.inaltime = inaltime
    def __str__(self):
        rez = Planta.__str__(self)
        rez += "\nculoare: " + self.culoare + "\ninaltime: " + str(self.inaltime)
        
class Conifer(Planta):
    def __init__(self, nume, clima, info, inaltime):
        super().__init__(nume, clima, info)
        self.inaltime = inaltime

idk = []
idk.append(Planta("lalea", "temperat", "..."))
idk.append(Trandafir("temperat", " ...", "rosu", 20))
idk.append(Trandafir("temperat", "... ", "albastru", 10))
idk.append(Trandafir("temperat", "... ", "rosu", 30))
idk.append(Conifer("pin", "tundra", "...", 10))
#print(idk)

plante = {}
for i in idk:
    if i.clima in plante:
        plante[i.clima].append(i.nume)
    else:
        plante[i.clima] = [i.nume]
for i in plante:
    print(i, ":\n")
    for j in plante[i]:
        print(j)
    print()

trandafiri = []
for i in idk:
    if type(i) == Trandafir:
        trandafiri.append(i)

culori = {}
for i in trandafiri:
    print(i.culoare)
    if i.culoare in culori:
        plante[i.culoare].append(i.inaltime)
    else:
        plante[i.culoare] = [i.inaltime]

for i in culori:
    print(i)
    for j in culori[i]:
        print(j)