from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField('Käyttäjänimi')
    password = PasswordField('Salasana')

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField('Nimi', [validators.Length(min=1)])
    username = StringField('Käyttäjänimi', [validators.Length(min=1)])
    password = PasswordField('Salasana', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Salasanat eivät täsmänneet toisiinsa')
    ])
    confirm = PasswordField('Kirjoita salasana uudelleen')

    class Meta:
        csrf = False
