#!/usr/bin/python3


""" State Module for HBNB project """


# from models.city import City  # use __init__.py version
# from models.engine.file_storage import FileStorage


from sqlalchemy.orm import relationship


from models.base_model import Base, BaseModel, models, sa


class State(BaseModel, Base):
    """ State class """

    if models.HBNB_TYPE_STORAGE == "db":
        __tablename__ = "states"

        name = sa.Column(
            "name",
            sa.String(128),
            nullable=False,
        )

        __cities = relationship(City, backref="state", cascade="all, delete")
    else:
        name = ""

'''
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
'''
