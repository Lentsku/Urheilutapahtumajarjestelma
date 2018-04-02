from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, validators

class PersonForm(FlaskForm):
    firstname = StringField('Etunimi', [validators.Length(min=1)])
    lastname = StringField('Sukunimi', [validators.Length(min=1)])
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
    lastFirstSearch = StringField('Sukunimi etunimi-haku')

    class Meta:
        csrf = False

class SelectOptionsForm(FlaskForm):
    optionsSelector = SelectField(
        'Valitse sarja',
        choices=[('add', 'Lisää tapahtumaan'), ('update', 'Muokkaa tietoja'),
                 ('delete', 'Poista tiedot')]
    )
    class Meta:
        csrf = False
