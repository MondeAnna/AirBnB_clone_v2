#!/usr/bin/python3


"""This module defines a base class for all models in our hbnb clone"""


from importlib import import_module
from datetime import datetime
import uuid


from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa


models = import_module("models")
Base = declarative_base() if models.STORAGE_TYPE == "db" else object


class BaseModel:
    """A base class for all hbnb models"""

    if models.STORAGE_TYPE == "db":
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
            self.__init_default()
        else:
            self.__init_kwargs(kwargs)

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

    def __eq__(self, other):
        """ensure two instances have the same id and were created at the same time"""

        return (
            self.id == other.id
            and self.__class__ == other.__class__
            and self.created_at == other.created_at
        )

    def __init_default(self):
        """Generates a new BaseModel object"""

        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __init_kwargs(self, kwargs):
        """
        Spawns an existing object

        Parameters
        ----------
        kwargs : Any
            keyword-to-value pairings used to deserialise
            and spawn existing objects
        """

        if kwargs.get("__class__"):
            del kwargs["__class__"]

        for key in kwargs.keys():
            if key.istitle():
                raise KeyError("__class__")

        if not kwargs.get("id"):
            kwargs["id"] = str(uuid.uuid4())

        kwargs["updated_at"] = datetime.now()

        if kwargs.get("created_at"):
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"],
                "%Y-%m-%dT%H:%M:%S.%f",
            )
        else:
            kwargs["created_at"] = kwargs["updated_at"]

        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""

        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return f"[{cls}] ({self.id}) {self.__dict__}"
