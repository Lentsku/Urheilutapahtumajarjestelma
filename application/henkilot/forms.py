from flask_wtf import FlaskForm
from wtforms import StringField

class HenkiloForm(FlaskForm):
    etunimi = StringField('Etunimi')
    sukunimi = StringField('Sukunimi')
    sukuEtu = StringField('SukuEtu')
    sahkoposti = StringField('Sähköposti')
    puhelin = StringField('Puhelin')
    osoite = StringField('Osoite')
    postinumero = StringField('Postinumero')
    postitoimipaikka = StringField('Postitoimipaikka')
    maa = StringField('Maa')

    class Meta:
        csrf = False
