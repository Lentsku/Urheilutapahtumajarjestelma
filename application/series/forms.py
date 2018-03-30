from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, FloatField, validators

class SeriesForm(FlaskForm):
    seriesName = StringField('Sarjan nimi')
    eventName = StringField('Tapahtuman nimi')
    startTime = DateTimeField('Lähtöaika')
    totalDistance = FloatField('Kokonaismatka')

    class Meta:
        csrf = False
