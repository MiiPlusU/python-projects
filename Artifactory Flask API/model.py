from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ArtifactLog(db.Model):
    __tablename__ = "artifact_logs"

    id = db.Column(db.Integer, primary_key=True)
    artifact_path = db.Column(db.String(255), nullable=False)
    action = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))