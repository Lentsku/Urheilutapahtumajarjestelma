from flask_wtf import FlaskForm
from wtforms import StringField, DateField, validators

class PersonForm(FlaskForm):
    firstname = StringField('Etunimi', [validators.Length(min=2)])
    lastname = StringField('Sukunimi', [validators.Length(min=3)])
    birthdate = DateField('Syntymäaika')
    email = StringField('Sähköposti')
    phone = StringField('Puhelin')
    address = StringField('Osoite')
    postalCode = StringField('Postinumero')
    postOffice = StringField('Postitoimipaikka')
    country = StringField('Maa')

    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    lastFirst = StringField('SukuEtu-haku', [validators.Length(min=5, message='Pituus 5 merkkiä. Kirjoita 3 sukunimen ensimmäistä kirjaina ja 2 etunimen ensimmäistä kirjainta, kirjainkoolla ei ole väliä')])

    class Meta:
        csrf = False
