#!/usr/bin/python3


"""City Module for HBNB project"""


from sqlalchemy.orm import relationship


from models.base_model import Base, BaseModel, models, sa
from models.place import Place


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    if models.HBNB_TYPE_STORAGE == "db":
        __tablename__ = "cities"

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

        places = relationship(Place, backref="cities", cascade="all, delete")
    else:
        name = state_id = ""
