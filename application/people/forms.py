from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PersonForm(FlaskForm):
    firstname = StringField('Etunimi', [validators.Length(min=2)])
    lastname = StringField('Sukunimi', [validators.Length(min=3)])
    email = StringField('Sähköposti')
    phone = StringField('Puhelin')
    address = StringField('Osoite')
    zipcode = StringField('Postinumero')
    postOffice = StringField('Postitoimipaikka')
    country = StringField('Maa')

    class Meta:
        csrf = False
