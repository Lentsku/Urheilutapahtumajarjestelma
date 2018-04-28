from application import db
from application.models import Base

from sqlalchemy.sql import text

class Series(Base):

    __tablename__ = 'Series'

    seriesName = db.Column(db.String(255), nullable=False)
    eventName = db.Column(db.String(255), nullable=False)
    startTime = db.Column(db.DateTime, index=True, nullable=False)
    totalDistance = db.Column(db.Float, nullable=False)

    registration = db.relationship('Registration', backref='Series', lazy=True)

    def __init__(self, seriesName, eventName, startTime, totalDistance):
        self.seriesName = seriesName
        self.eventName = eventName
        self.startTime = startTime
        self.totalDistance = totalDistance

    def get_id(self):
        return self.id

    @staticmethod
    def find_amount_of_people_registered():
        stmt = text(
            'SELECT "Series".seriesName, "Series".eventName, "Series".startTime, "Series".totalDistance, COUNT("Registration".person_id) AS registered'
            ' FROM "Series"'
            ' LEFT JOIN "Registration" ON "Registration".series_id = "Series".id'
            ' GROUP BY "Series".id'
            ' ORDER BY "Series".startTime DESC'
        )
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({'seriesName':row[0], 'eventName':row[1], 'startTime':row[2], 'totalDistance':row[3], 'registered':row[4]})

        return response
