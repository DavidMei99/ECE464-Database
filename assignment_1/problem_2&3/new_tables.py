# ECE464 Database Problem Set 1
# Di Mei
# new_tables.py (for Part 3)
# create improved tables

import os, sys
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///new_sailors.db')
Base = declarative_base()

# table 1: Sailors
class Sailors(Base):
    __tablename__ = 'sailors'
    sid = Column(Integer, primary_key=True)
    sname = Column(String(30), nullable=False)
    rating = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False) # newly added field: personal phone number
    
    def __repr__(self):
        return "<Sailor(id=%s, name='%s', rating=%s, age=%s)>" % (self.sid, self.sname, self.rating, self.age)

# table 2: Reserves
class Reserves(Base):
    __tablename__ = 'reserves'
    __table_args__ = (PrimaryKeyConstraint('sid', 'bid', 'day'), {})
    sid = Column(Integer, ForeignKey('sailors.sid'))
    bid = Column(Integer, ForeignKey('boats.bid'))
    day = Column(String(10), nullable=False)
    condition = Column(String(40), nullable=False) # newly added field: the general condition of a boat
    
    def __repr__(self):
        return "<Reservation(sid=%s, bid=%s, day=%s)>" % (self.sid, self.bid, self.day)

# table 3: Boats
class Boats(Base):
    __tablename__ = 'boats'
    bid = Column(Integer, primary_key=True)
    bname = Column(String(20), nullable=False)
    color = Column(String(10), nullable=False)
    length = Column(Integer, nullable=False)
    numrent = Column(Integer, nullable=False) # newly added field: number of rental times
    daylast = Column(String(10)) # newly added field: date of the last maintenance
    
    def __repr__(self):
        return "<Boat(id=%s, name='%s', color=%s, length=%s)>" % (self.bid, self.bname, self.color, self.length)

# table 4: Employees (newly added class)
class Employees(Base):
    __tablename__ = 'employees'
    eid = Column(Integer, primary_key=True)
    ename = Column(String(30), nullable=False)
    jobtitle = Column(String(20), nullable=False)
    phone = Column(Integer, nullable=False)
    ssn = Column(String(11), nullable=False)
    salary = Column(Integer, nullable=False) # hourly salary
    
    def __repr__(self):
        return "<Employee(id=%s, name='%s', job=%s, phone=%s)>" % (self.eid, self.ename, self.jobtitle, self.phone)
    
# table 5: Maintenance (newly added class)
class Maintenance(Base):
    __tablename__ = 'maintenance'
    __table_args__ = (PrimaryKeyConstraint('eid', 'bid', 'mdate', 'cost'), {})
    eid = Column(Integer, ForeignKey('employees.eid'))
    bid = Column(Integer, ForeignKey('boats.bid'))
    mdate = Column(String(10), nullable=False)
    cost = Column(Integer, nullable=False)
    
    def __repr__(self):
        return "<Maintenance(eid=%s, bid=%s, mdate=%s)>" % (self.eid, self.bid, self.mdate)
    
# issue "CREATE" statement for all tables
Base.metadata.create_all(engine)
