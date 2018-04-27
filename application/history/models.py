from application import db
from application.models import Base
from sqlalchemy.orm import backref

class History(Base):

    __tablename__ = 'History'

    participationMarks = db.Column(db.Integer, default=0)
    achievementMarks = db.Column(db.Integer, default=0)
    tours = db.Column(db.Integer, default=0)
    skiingTimes = db.Column(db.Integer, default=0)
    bikingTimes = db.Column(db.Integer, default=0)
    rowingTimes = db.Column(db.Integer, default=0)
    joggingTimes = db.Column(db.Integer, default=0)

    person_id = db.Column(db.Integer, db.ForeignKey('Person.id'))
    person = db.relationship('Person', backref=backref('History', uselist=False))

    def get_id(self):
        return self.id
