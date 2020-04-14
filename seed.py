from models import User, db, Post, Tag, PostTag
from app import app

db.drop_all()
db.create_all()

User.query.delete()

test1 = User(first_name='John', last_name='Smith')
test2 = User(first_name='Bobby', last_name='Wilson')
test3 = User(first_name='Orin', last_name='Anderson')


db.session.add_all([test1, test2, test3])
db.session.commit()


test1_1 = Post(title='Test_1', content='THIS_IS_A_TEST_CONTENT', user_id=1)
test2_2 = Post(title='Test_2', content='THIS_IS_A_TEST_CONTENT', user_id=2)
tag1 = Tag(name='Sunny', post[PostTag(post_id=test1.id, tag_id=tag1.id)])


db.session.add_all([test1_1, test2_2, tag1])
db.session.commit()