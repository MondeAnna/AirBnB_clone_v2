#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel, sa


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
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
