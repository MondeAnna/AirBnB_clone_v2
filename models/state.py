#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel, sa
from models.city import City  # use __init__.py version


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = sa.Column(
        "name",
        sa.String(128),
        nullable=False,
    )

    __cities = relationship(City, backref="state", cascade="all, delete")
