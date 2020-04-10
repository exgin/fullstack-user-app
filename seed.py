from models import User, db
from app import app

db.drop_all()
db.create_all()

User.query.delete()

test1 = User(first_name='John', last_name='Smith')
test2 = User(first_name='Bobby', last_name='Wilson')
test3 = User(first_name='Orin', last_name='Anderson')

db.session.add(test1)
db.session.add(test2)
db.session.add(test3)

db.session.commit()