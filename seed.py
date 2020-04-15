from models import User, db, Post, Tag, PostTag
from app import app

db.drop_all()
db.create_all()

user1 = User(first_name='John', last_name='Smith')
user2 = User(first_name='Bobby', last_name='Wilson')
user3 = User(first_name='Orin', last_name='Anderson')

post1 = Post(title='POST 1', content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
post2 = Post(title='POST 2', content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
post3 = Post(title='POST 3', content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")


user1.post.append(post1)
user2.post.append(post2)
user3.post.append(post3)

db.session.add_all([user1, user2, user3])
db.session.commit()

all_posts = Post.query.all()

post1 = all_posts[0]
post2 = all_posts[1]
post3 = all_posts[2]

tag1 = Tag(name="Sunny")
tag2 = Tag(name="Cloudy")
tag3 = Tag(name="Love")

post1.tag.append(tag1)
post2.tag.append(tag2)
post3.tag.append(tag3)

db.session.add_all([post1, post2, post3])
db.session.commit()
