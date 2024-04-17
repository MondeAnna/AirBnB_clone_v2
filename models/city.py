#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import Base, BaseModel, sa


class City(BaseModel, Base):
    ...
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

'''
    name = sa.Column(
        "name",
        sa.String(128),
        nullable=False,
    )

    state_id = sa.Column(
        "state_id",
        sa.String(60),
        sa.ForeignKey("states.id"),
        nullable=False,
    )
'''
