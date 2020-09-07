from core.db import Base
from sqlalchemy import Column, Integer, Boolean, DateTime, String, func


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, nullable=True)
    token = Column(String, nullable=True)

    # Debug time
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime,
                        server_default=func.now(),
                        onupdate=func.now(),
                        nullable=False)
    # Flags
    started = Column(Boolean, nullable=False, default=False)
    banned = Column(Boolean, nullable=False, default=False)
    broadcast_sent = Column(Boolean, nullable=False, default=False)
    last_update = Column(DateTime)

    # Permanent settings
    admin = Column(Boolean, nullable=False, default=False)
    notifications_enabled = Column(Boolean, nullable=False, default=True)

    # Chat logic
    expected_input = Column(String)

    def __init__(self, user_id: int, name: str):
        self.id = user_id
        self.name = name

    def __repr__(self):
        """Print as string."""
        return f"User with Id: {self.id}, name: {self.name}"

    def delete(self):
        """Delete the user."""
        self.started = False
        self.username = "GDPR removed user"
        self.name = "GDPR removed user"
        self.locale = "English"
        self.european_date_format = False
        self.notifications_enabled = False
