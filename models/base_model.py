#!/usr/bin/python3


"""This module defines a base class for all models in our hbnb clone"""


from importlib import import_module
from datetime import datetime
import uuid


from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa


models = import_module("models")
Base = declarative_base() if models.HBNB_TYPE_STORAGE == "db" else object


class BaseModel:
    """A base class for all hbnb models"""

    id = sa.Column(
        "id",
        sa.String(60),
        nullable=False,
        primary_key=True,
    )

    created_at = sa.Column(
        "created_at",
        sa.DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at = sa.Column(
        "updated_at",
        sa.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    def __init__(self, *args, **kwargs):
        """
        Spawns an existing object or generates a new one

        Parameters
        ----------
        args : Any
            unused

        kwargs : Any
            keyword-to-value pairings used to deserialise
            and spawn existing objects
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            del kwargs["__class__"]

            kwargs["updated_at"] = datetime.now()
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"],
                "%Y-%m-%dT%H:%M:%S.%f",
            )

            self.__dict__.update(kwargs)

    def delete(self):
        """Deletes current instance from storage"""

        models.storage.delete(self)

    def save(self):
        """Updates updated_at with current time when instance is changed"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""

        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__": (str(type(self)).split(".")[-1]).split("'")[0]})
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        if "_sa_instance_state" in dictionary:
            dictionary.pop("_sa_instance_state")

        return dictionary

    def __str__(self):
        """Returns a string representation of the instance"""

        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return f"[{cls}] ({self.id}) {self.__dict__}"

    def __eq__(self, other):
        """ensure two instances have the same id and were created at the same time"""

        return (
            self.id == other.id
            and self.__class__ == other.__class__
            and self.created_at == other.created_at
        )
