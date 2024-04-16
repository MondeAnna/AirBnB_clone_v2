#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy.orm import Session
import sqlalchemy as sa
import os


USER = os.getenv("HBNB_MYSQL_USER")
PWD = os.getenv("HBNB_MYSQL_PWD")
HOST = os.getenv("HBNB_MYSQL_HOST", "localhost")
DB = os.getenv("HBNB_MYSQL_DB")
ENV = os.getenv("HBNB_ENV", "test")


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

        metadata = sa.MetaData()

        # name this properly please
        if ENV == "test !!!! fix me":
            metadata.reflect(self.__engine)
            metadata.drop_all(self.__engine)

        metadata.create_all(self.__engine)

    def all(self, cls=None):
        if cls:
            return self.__session.query(cls).all()  # see if .all() is needed
        return self.__session.query().all()  # see if this workds

    def new(self, obj):
        self.__session.add(obj)
        """ add the object to the current database session (self.__session) """

    def save(self):
        self.__session.commit()
        """ commit all changes of the current database session """
        ...

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            ...

    def reload(self):
        ...
