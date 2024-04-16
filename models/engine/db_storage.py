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

        # name this properly please
        if ENV == "test !!!! fix me":
            metadata = sa.MetaData()
            metadata.reflect(self.__engine)
            metadata.drop_all(self.__engine)
