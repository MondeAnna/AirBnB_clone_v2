#!/usr/bin/python3


""" Review module for the HBNB project """


from models.base_model import Base, BaseModel, models, sa


class Review(BaseModel, Base):
    """ Review classto store review information """

    if models.HBNB_TYPE_STORAGE == "db":
        __tablename__ = "reviews"

        text = sa.Column(
            "text",
            sa.String(1024),
            nullable=False,
        )

        place_id = sa.Column(
            "place_id",
            sa.String(60),
            sa.ForeignKey("places.id"),
            nullable=False,
        )

        user_id = sa.Column(
            "user_id",
            sa.String(60),
            sa.ForeignKey("users.id"),
            nullable=False,
        )

    else:
        place_id = ""
        user_id = ""
        text = ""
