from flask_wtf import FlaskForm
from wtforms import StringField

class EtunimiForm(FlaskForm):
    name = StringField('Etunimi')

    class Meta:
        csrf = False
