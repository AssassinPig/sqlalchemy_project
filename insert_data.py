from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_table import Address, Base, Person

engine = create_engine('postgresql://assassinpig:123456@localhost/flaskr')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
new_person = Person(name='new person')
session.add(new_person)
session.commit()

new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()
