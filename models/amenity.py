#!/usr/bin/python3


"""Amenity Module for HBNB project"""


from models.base_model import Base, BaseModel, models, sa


class Amenity(BaseModel, Base):
    """The amenity class, focused on the amenity's name"""

    if models.HBNB_TYPE_STORAGE == "db":
        __tablename__ = "amenities"

        name = sa.Column(
            "name",
            sa.String(128),
            nullable=False,
        )
    else:
        name = ""
