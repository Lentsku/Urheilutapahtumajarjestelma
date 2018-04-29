from application import db
from application.models import Base

class Checkpoint(Base):

    __tablename__ = 'Checkpoint'

    checkpointName = db.Column(db.String(255), nullable=False)
    isGoal = db.Column(db.Boolean, nullable=False)
    distance = db.Column(db.Float, nullable=False)
