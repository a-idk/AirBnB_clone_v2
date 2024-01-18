#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import shlex as sh


class State(BaseModel):
    """ State class """
    __tablename__ = "states"  # name of table
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City',
            backref='state',
            cascade='all, delete-orphan'
            )

    @property
    def cities(self):
        store = models.storage.all()
        out_list = []
        new_list = []

        for key in models.storage.all():
            city = key.replace('.', ' ')
            city = sh.split(city)

            if (city[0] == 'City'):

                new_list.append(models.storage.all()[key])

                for indx in new_list:
                    if (indx.state_id == self.id):
                        out_list.append(indx)
                return (out_list)
