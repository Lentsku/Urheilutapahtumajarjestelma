from application import db

class Henkilo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    etunimi = db.Column(db.String(63), nullable=False)
    sukunimi = db.Column(db.String(63), nullable=False)
    sukuEtu = db.Column(db.String(7), nullable=False)
    sahkoposti = db.Column(db.String(255), nullable=True)
    puhelin = db.Column(db.String(255), nullable=True)
    osoite = db.Column(db.String(255), nullable=False)
    postinumero = db.Column(db.String(63), nullable=False)
    postitoimipaikka = db.Column(db.String(144), nullable=False)
    maa = db.Column(db.String(144), nullable=True)

    def __init__(self, etunimi, sukunimi, sukuEtu, sahkoposti, puhelin, osoite, postinumero, postitoimipaikka, maa):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.sukuEtu = sukuEtu # Kolme ensimmäistä sukunimen kirjainta ja kaksi ensimmäistä etunimen kirjainta
        self.sahkoposti = sahkoposti
        self.puhelin = puhelin
        self.osoite = osoite
        self.postinumero = postinumero
        self.postitoimipaikka = postitoimipaikka
        self.maa = maa
