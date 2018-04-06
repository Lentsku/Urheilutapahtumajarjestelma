from application.people.models import Person
from application.personSeries.models import PersonSeries
from application.series.models import Series

def findRegistrationList(personId):
    personSeriesList = PersonSeries.query.filter_by(person_id = personId).all()
    seriesList = []

    for personSeries in personSeriesList:
        seriesId = personSeries.series_id
        series = Series.query.filter_by(id = seriesId).first()
        seriesList.append(series)

    return seriesList
