#!/usr/bin/python3
"""This module defines a class User"""


from sqlalchemy.orm import relationship


from models.base_model import Base, BaseModel, models, sa
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if models.STORAGE_TYPE == "db":
        __tablename__ = "users"

        email = sa.Column(
            "email",
            sa.String(128),
            nullable=False,
        )

        password = sa.Column(
            "password",
            sa.String(128),
            nullable=False,
        )

        first_name = sa.Column(
            "first_name",
            sa.String(128),
            nullable=False,
        )

        last_name = sa.Column(
            "last_name",
            sa.String(128),
            nullable=False,
        )

        places = relationship(Place, backref="user", cascade="all, delete")
        reviews = relationship(Review, backref="user", cascade="all, delete")
    else:
        email = password = first_name = last_name = ""
