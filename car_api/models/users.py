from sqlalchemy import Column, Integer, String, DateTime, func
from car_api.models.base import Base

# Traditional way to create a model for database table in SQLAlchemy
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(
        DateTime,
        server_default=func.now()
    )
    updated_at = Column(
        DateTime,
        server_default=func.now(), 
        server_onupdate=func.now()
    )
