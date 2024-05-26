#!/usr/bin/python3


""" Place Module for HBNB project """


from sqlalchemy.orm import relationship


from models.base_model import Base, BaseModel, models, sa
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """

    if models.STORAGE_TYPE == "db":
        __tablename__ = "places"

        city_id = sa.Column(
            "city_id",
            sa.String(60),
            sa.ForeignKey("cities.id"),
            nullable=False,
        )

        user_id = sa.Column(
            "user_id",
            sa.String(60),
            sa.ForeignKey("users.id"),
            nullable=False,
        )

        name = sa.Column(
            "name",
            sa.String(128),
            nullable=False,
        )

        description = sa.Column(
            "description",
            sa.String(1024),
            nullable=False,
        )

        number_rooms = sa.Column(
            "number_rooms",
            sa.Integer,
            default=0,
            nullable=False,
        )

        number_bathrooms = sa.Column(
            "number_bathrooms",
            sa.Integer,
            default=0,
            nullable=False,
        )

        max_guest = sa.Column(
            "max_guest",
            sa.Integer,
            default=0,
            nullable=False,
        )

        price_by_night = sa.Column(
            "price_by_night",
            sa.Integer,
            default=0,
            nullable=False,
        )

        latitude = sa.Column(
            "latitude",
            sa.Float,
            nullable=False,
        )

        longitude = sa.Column(
            "longitude",
            sa.Float,
            nullable=False,
        )

        amenity_id = sa.Column(
            "amenity_id",
            sa.String(60),
            sa.ForeignKey("amenities.id"),
            nullable=False,
        )

        reviews = relationship(Review, backref="place", cascade="all, delete")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
