# ECE464 Database Problem Set 1
# Di Mei
# new_insert.py (for Part 3)
# insert some sample items

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from new_tables import Base, Sailors, Reserves, Boats, Employees, Maintenance

# an engine, which the Session will use for connection resourses
engine = create_engine('sqlite:///new_sailors.db')
# create a configured "Session" class
Session = sessionmaker(bind=engine)
# create a Session
session = Session()

sailor = Sailors(sid=19,sname='David',rating=7,age=45.0,phone=1112223000)
session.add(sailor)
sailor = Sailors(sid=20,sname='Joseph',rating=1,age=33.0,phone=1002223333)
session.add(sailor)
sailor = Sailors(sid=21,sname='Kenny',rating=8,age=55.5,phone=1112223000)
session.add(sailor)
session.commit()

reserve = Reserves(sid=19,bid=101,day='1998/10/10',condition='good (no maintenance required)')
session.add(reserve)
reserve = Reserves(sid=20,bid=101,day='1998/11/15',condition='good but required being painted')
session.add(reserve)
reserve = Reserves(sid=21,bid=102,day='1998/8/10',condition='good (no maintenance required)')
session.add(reserve)
session.commit()

boat = Boats(bid=101,bname='Ark',color='blue',length=1000,numrent=2, daylast='1998/11/16')
session.add(boat)
boat = Boats(bid=102,bname='Yggresil',color='green',length=1000,numrent=1,daylast='1998/8/9')
session.add(boat)
session.commit()

employee = Employees(eid=900,ename='Gabriel',jobtitle='senior technician',phone=1002003000,ssn='111-99-1111',salary=1000)
session.add(employee)
employee = Employees(eid=999,ename='Keter',jobtitle='senior technician',phone=4005006000,ssn='222-99-2222',salary=1000)
session.add(employee)
session.commit()

maintenance = Maintenance(eid=900,bid=101,mdate='1998/11/16',cost=99)
session.add(maintenance)
maintenance = Maintenance(eid=999,bid=102,mdate='1998/8/9',cost=199)
session.add(maintenance)
