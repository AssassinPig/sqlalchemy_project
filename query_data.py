from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_table import Address, Base, Person

engine = create_engine('postgresql://assassinpig:123456@localhost/flaskr')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

session.query(Person).all()

person = session.query(Person).first()
#print person.name

session.query(Address).filter(Address.person==person).all()
address = session.query(Address).filter(Address.person==person).one()
#print address.post_code
