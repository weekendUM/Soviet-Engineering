class copil:
    UUID= '1234AV'
    name= 'Grigore Rasputin'
    class adresa:
        Country= 'Romania'
        City= 'Bucuresti'
        street= 'lala'
        number= '241'
    cadouri=[]
class cadou:
    def init(self, obiect, cantitate, adjective, UID):
        self.obiect= obiect
        self.cantitate= cantitate
        self.adjective= adjective
        self.UID= UID


test = cadou('a')