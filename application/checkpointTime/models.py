from application import db
from application.models import Base

class CheckpointTime(Base):

    __tablename__ = 'CheckpointTime'

    checkpointTime = db.Column(db.DateTime, index=True, nullable=True)
