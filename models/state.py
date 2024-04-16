#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel, sa


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = sa.Column(
        "name",
        sa.String(128),
        nullable=False,
    )
