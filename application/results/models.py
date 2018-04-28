from application import db
from application.models import Base
from sqlalchemy.orm import backref

class Results(Base):

    __tablename__ = 'Results'

    placement = db.Column(db.Integer, nullable=True)
    startTime = db.Column(db.DateTime, index=True, nullable=False)
    finishTime = db.Column(db.DateTime, index=True, nullable=True)
    achievementMark = db.Column(db.Boolean, default=False)

    registration_id = db.Column(db.Integer, db.ForeignKey('Registration.id'))
    registration = db.relationship('Registration', backref=backref('Results', uselist=False))

    def __init__(self, placement, startTime, finishTime, achievementMark):
        self.placement = placement
        self.startTime = startTime
        self.finishTime = finishTime
        self.achievementMark = achievementMark

    def get_id(self):
        return self.id
