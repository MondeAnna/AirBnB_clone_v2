#!/usr/bin/python3


""" State Module for HBNB project """


from sqlalchemy.orm import relationship


from models.base_model import Base, BaseModel, models, sa
from models.city import City


class State(BaseModel, Base):
    """ State class """

    if models.STORAGE_TYPE == "db":
        __tablename__ = "states"

        name = sa.Column(
            "name",
            sa.String(128),
            nullable=False,
        )

        __cities = relationship(City, backref="state", cascade="all, delete")
    else:
        name = ""

    @property
    def cities(self):
        """
        Provides a map of City objects from storage linked
        to the current State
        """

        FileStorage = models.engine.file_storage.FileStorage

        if models.storage is FileStorage:
            return State.__cities

        stored = models.storage.all(City)

        return [
            city for id_, city in stored.items()
            if self.id in id_
        ]
