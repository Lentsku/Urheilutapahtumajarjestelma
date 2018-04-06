from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, validators

class PersonForm(FlaskForm):
    firstname = StringField('Etunimi', [validators.Length(min=1)])
    lastname = StringField('Sukunimi', [validators.Length(min=1)])
    birthdate = DateField('Syntymäaika', [validators.Length(min=1)])
    email = StringField('Sähköposti', [validators.Length(min=1)])
    phone = StringField('Puhelin', [validators.Length(min=1)])
    address = StringField('Osoite', [validators.Length(min=1)])
    postalCode = StringField('Postinumero', [validators.Length(min=1)])
    postOffice = StringField('Postitoimipaikka', [validators.Length(min=1)])
    country = StringField('Maa', [validators.Length(min=1)])

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
