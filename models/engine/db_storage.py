#!/usr/bin/python3


"""This module defines a class to manage db storage for hbnb clone"""


from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import sqlalchemy as sa
import os


from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User


from models.base_model import Base


USER = os.getenv("HBNB_MYSQL_USER", "hbnb_test")
PWD = os.getenv("HBNB_MYSQL_PWD", "hbnb_test_pwd")
HOST = os.getenv("HBNB_MYSQL_HOST", "localhost")
DB = os.getenv("HBNB_MYSQL_DB", "hbnb_test_db")
ENV = os.getenv("HBNB_ENV", "test")


MODELS = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}


class DBStorage:
    """This class manages db storage for hbnb clone"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = sa.create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                USER, PWD, HOST, DB
            ),
            pool_pre_ping=True,
        )

        self.__session = Session(bind=self.__engine)

        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        if cls:
            _all = self.__session.query(cls).all()
        else:
            _all = [
                obj
                for model in MODELS.values()
                for objs in self.__session.query(model).all()
                for obj in objs
            ]

        return {
            f"{obj.__class__.__name__}.{obj.id}": obj
            for obj in _all
        }

    def close(self):
        """Close Database Connection"""

        self.__session.close()

    def delete(self, obj=None):
        """Delete from current db session if `obj` is not None"""

        try:
            self.__session.delete(obj)
        except Exception:
            ...

    def new(self, obj):
        """Add object to current db session"""

        self.__session.add(obj)

    def reload(self):
        """Create a new Database connection, reloading data there from"""

        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def save(self):
        """Commit all changes of current db session"""

        self.__session.commit()
