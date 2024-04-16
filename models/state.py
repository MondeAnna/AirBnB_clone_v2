#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel, sa
from models.city import City  # use __init__.py version
from models.engine import FileStorage  # use __init__.py version


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = sa.Column(
        "name",
        sa.String(128),
        nullable=False,
    )

    __cities = relationship(City, backref="state", cascade="all, delete")

    @property
    def cities(self):
        from models import storage
        if storage is FileStorage:
            return State.__cities
        stored = storage.all(City)
        return {
            identifier: obj
            for identifier, obj in stored.items()
            if self.id in identifier
        }
