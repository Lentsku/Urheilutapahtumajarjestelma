from application import db
from application.models import Base

class PersonSeries(Base):

    __tablename__ = 'PersonSeries'

    competitorNumber = db.Column(db.Integer, nullable=False)
    person_id = db.Column('Person_id', db.Integer, db.ForeignKey(
        'Person.id', primary_key=True), nullable=False)
    series_id = db.Column('Series_id', db.Integer, db.ForeignKey(
        'Series.id', primary_key=True), nullable=False)
    results_id = db.Column('Results_id', db.Integer, db.ForeignKey(
        'Results.id', primary_key=True), nullable=False)

    def __init__(self, competitorNumber):
        self.competitorNumber = competitorNumber
