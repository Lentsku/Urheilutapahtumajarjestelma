from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, FloatField, SelectField, validators


from application.series.models import Series

class SeriesForm(FlaskForm):
    seriesName = StringField('Sarjan nimi')
    eventName = StringField('Tapahtuman nimi')
    startTime = DateTimeField('Lähtöaika')
    totalDistance = FloatField('Kokonaismatka')

    class Meta:
        csrf = False

class SelectSeriesForm(FlaskForm):
    series = Series.query.all()

    seriesList = []
    for item in series:
        seriesList.append(tuple((item.id, item.startTime.strftime('%Y') + ' '
                                 + item.eventName + ' ' + item.seriesName)))

    seriesSelector = SelectField(
        'Valitse sarja',
        choices=seriesList
    )
    class Meta:
        csrf = False
