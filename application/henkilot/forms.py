from flask_wtf import FlaskForm
from wtforms import StringField, validators

class HenkiloForm(FlaskForm):
    etunimi = StringField('Etunimi', [validators.Length(min=1)])
    sukunimi = StringField('Sukunimi', [validators.Length(min=1)])
    sukuEtu = StringField('SukuEtu')
    sahkoposti = StringField('Sähköposti')
    puhelin = StringField('Puhelin')
    osoite = StringField('Osoite')
    postinumero = StringField('Postinumero')
    postitoimipaikka = StringField('Postitoimipaikka')
    maa = StringField('Maa')

    class Meta:
        csrf = False
