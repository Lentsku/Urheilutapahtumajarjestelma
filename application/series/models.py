from application import db

from application.personSeries.models import PersonSeries

class Series(db.Model):

    __tablename__ = 'Series'

    id = db.Column(db.Integer, primary_key=True)
    seriesName = db.Column(db.String(255), nullable=False)
    eventName = db.Column(db.String(255), nullable=False)
    startTime = db.Column(db.DateTime, index=True, nullable=False)
    totalDistance = db.Column(db.Float, nullable=False)

    personSeries = db.relationship('PersonSeries', backref='Series', lazy=True)

    def __init__(self, seriesName, eventName, startTime, totalDistance):
        self.seriesName = seriesName
        self.eventName = eventName
        self.startTime = startTime
        self.totalDistance = totalDistance

    def get_id(self):
        return self.id
