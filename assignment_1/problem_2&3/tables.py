# ECE464 Database Problem Set 1
# Di Mei
# tables.py (for Part 2)
# create tables

import os, sys
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///sailors.db')
Base = declarative_base()

# table 1: Sailors
class Sailors(Base):
    __tablename__ = 'sailors'
    sid = Column(Integer, primary_key=True)
    sname = Column(String(30), nullable=False)
    rating = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    
    def __repr__(self):
        return "<Sailor(id=%s, name='%s', rating=%s, age=%s)>" % (self.sid, self.sname, self.rating, self.age)

# table 2: Reserves
class Reserves(Base):
    __tablename__ = 'reserves'
    __table_args__ = (PrimaryKeyConstraint('sid', 'bid', 'day'), {})
    sid = Column(Integer, ForeignKey('sailors.sid'))
    bid = Column(Integer, ForeignKey('boats.bid'))
    day = Column(String(10))
    
    def __repr__(self):
        return "<Reservation(sid=%s, bid=%s, day=%s)>" % (self.sid, self.bid, self.day)

# table 3: Boats
class Boats(Base):
    __tablename__ = 'boats'
    bid = Column(Integer, primary_key=True)
    bname = Column(String(20), nullable=False)
    color = Column(String(10), nullable=False)
    length = Column(Integer, nullable=False)
    
    def __repr__(self):
        return "<Boat(id=%s, name='%s', color=%s, length=%s)>" % (self.bid, self.bname, self.color, self.length)

# issue "CREATE" statement for all tables
Base.metadata.create_all(engine)
