import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


favorite_characters = Table(
    "favorite_characters",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("character_id", ForeignKey("characters.id")),
)

favorite_planets = Table(
    "favorite_planets",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("planet_id", ForeignKey("planets.id")),
)

favorite_starships = Table(
    "favorite_starships",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("planet_id", ForeignKey("starships.id")),
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique = True)
    password = Column(String(50), nullable=False)
    favorite_characters = relationship("characters", secondary = favorite_characters)
    favorite_planets = relationship("planets", secondary = favorite_planets)
    favorite_starships = relationship("starships", secondary = favorite_starships)


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)
    Gender = Column(String(50), nullable=False)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique = True)
    population = Column(BigInteger, nullable=True)
    rotation_period = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=True)
    gravity = Column(String(50), nullable=True)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique = True)
    speed = Column(Integer, nullable=True)
    passengers = Column(BigInteger, nullable=True)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')



# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(50))
#     street_number = Column(String(50))
#     post_code = Column(String(50), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}