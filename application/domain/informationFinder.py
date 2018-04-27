from application.people.models import Person
from application.registration.models import Registration
from application.series.models import Series

def findRegistrationList(personId):
    registrationList = Registration.query.filter_by(person_id = personId).all()
    seriesList = []

    for registration in registrationList:
        seriesId = registration.series_id
        series = Series.query.filter_by(id = seriesId).first()
        seriesList.append(series)

    return seriesList
