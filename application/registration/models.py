from application import db
from application.models import Base

class Registration(Base):

    __tablename__ = 'Registration'

    competitorNumber = db.Column(db.Integer, nullable=False)
    person_id = db.Column('Person_id', db.Integer, db.ForeignKey(
        'Person.id', primary_key=True), nullable=False)
    series_id = db.Column('Series_id', db.Integer, db.ForeignKey(
        'Series.id', primary_key=True), nullable=False)

    def __init__(self, competitorNumber):
        self.competitorNumber = competitorNumber
