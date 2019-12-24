# ECE464 Database Problem Set 1
# Di Mei
# insert.py (for Part 2)
# test of query samples (query 5, 6, 7 in Part 1)

from tables import Base, Sailors, Reserves, Boats
from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sailors.db')
Session = sessionmaker(bind = engine)
session = Session()

# compare sql query results generated by raw mysql queries and sqlalchemy objects
def check(raw_query, orm_result):
    # store results in lists first
    raw_list, new_list = [], []
    with engine.connect() as connection:
        raw_result = connection.execute(raw_query)
        for x in raw_result:
            raw_list.append(x)
    for x in orm_result:
        new_list.append(x)
    # if generated results are different, report AssertionError
    assert raw_list == new_list

# check query 5 in part 1
def test5():
    q = session.query(Reserves.bid, func.count('*').label('c')).group_by(Reserves.bid).order_by(desc('c')).limit(1)
    raw_query = "SELECT bid, count(bid) as num_reserves FROM reserves \
              GROUP BY bid ORDER BY num_reserves DESC LIMIT 1;"
    check(raw_query, q)

# check query 6 in part 1
def test6():
    q1 = session.query(Boats.bid).filter(Boats.color == "red")
    q2 = session.query(Reserves.sid).filter(Reserves.bid.in_(q1))
    q3 = session.query(Sailors.sid, Sailors.sname).filter(Sailors.sid.notin_(q2))
    raw_query = "SELECT sid, sname FROM sailors WHERE sid \
              NOT IN (SELECT r.sid \
              FROM reserves r INNER JOIN boats b ON r.bid = b.bid \
              WHERE color = 'red');"
    check(raw_query, q3)

# check query 7 in part 1
def test7():
    q = session.query(func.avg(Sailors.age)).filter(Sailors.rating == 10).all()
    raw_query = "SELECT AVG(age) FROM sailors WHERE rating = '10';"
    check(raw_query, q)

if  __name__ == "__main__":
    test5()
    test6()
    test7()