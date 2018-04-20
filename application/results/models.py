from application import db
from application.models import Base

from application.personSeries.models import PersonSeries

class Results(Base):

    __tablename__ = 'Results'

    placement = db.Column(db.Integer, nullable = True)
    startTime = db.Column(db.DateTime, index=True, nullable=False)
    finishTime = db.Column(db.DateTime, index=True, nullable=True)
    achievementMark = db.Column(db.Boolean, default=False)

    personSeries = db.relationship('PersonSeries', backref='Series', lazy=True)
