"""Blogly application."""

from flask import Flask, render_template, redirect, request, flash
from models import db, connect_db, User, Post, Tag, PostTag
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'sam123'
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

@app.route('/')
def home_app():
    """Display all users & add user btn"""
    users = User.query.order_by(User.last_name, User.first_name).all()

    return render_template('index.html', users=users)

@app.route('/users/new')
def add_user():
    """Show user form"""

    return render_template('add-user.html')

@app.route('/users/new', methods=['POST'])
def handle_add_user():
    """Handle the user form for creating a new user"""
    new_user = User(first_name=request.form['first_name'], last_name=request.form['last_name'], image_url=request.form['image_url'])
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show a specific user details"""
    user = User.query.get_or_404(user_id)

    return render_template("show-user.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def edit_show_user(user_id):
    """Hanlde the logic for editing a user in the database"""
    edited_user = User.query.get_or_404(user_id)

    edited_user.first_name = request.form['first_name']
    edited_user.last_name = request.form['last_name']
    edited_user.image_url = request.form['image_url']

    db.session.add(edited_user)
    db.session.commit()

    return redirect('/')

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Show edit user form & edit the db"""
    user = User.query.get_or_404(user_id)

    return render_template('edit-user.html', user=user)

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """Delete a user from my database"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/')

# Post Routes #
@app.route('/users/<int:user_id>/posts/new')
def show_user_post_form(user_id):
    """Show user post form"""
    user = User.query.get_or_404(user_id)

    return render_template('add-post-user.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def handle_user_post(user_id):
    """Handle user posts"""
    user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['post-title'], content=request.form['post-content'], user_id=user_id)

    db.session.add(new_post)
    db.session.commit()
    
    return redirect(f"/users/{user_id}")

@app.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """Delete a specific post"""
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")

@app.route('/post/<int:post_id>')
def show_post_details(post_id):
    """Show our post details"""
    post = Post.query.get_or_404(post_id)

    return render_template('post-user.html', post=post)

@app.route('/posts')
def show_all_posts():
    """Show every user post"""
    post = Post.query.all()

    return render_template('all-posts.html', post=post)

@app.route('/post/<int:post_id>/edit')
def show_edit_post(post_id):
    """Show user the form to edit a post"""
    post = Post.query.get_or_404(post_id)

    return render_template('edit-post.html', post=post)

@app.route('/post/<int:post_id>/edit', methods=['POST'])
def handle_edit_post(post_id):
    """Handle post request & logic for user posts"""
    edited_post = Post.query.get_or_404(post_id)

    edited_post.title = request.form['post-title']
    edited_post.content = request.form['post-content']

    db.session.add(edited_post)
    db.session.commit()

    return redirect(f"/users/{edited_post.user_id}")

# TAGS
@app.route('/tags')
def show_all_tags():
    """Show all tags"""
    tags = Tag.query.all()

    return render_template('all-tags.html', tags=tags)

@app.route('/tags/new')
def add_new_tag():
    """Show add new tag form"""

    return render_template('create-tag.html')

@app.route('/tags/new', methods=['POST'])
def handle_add_new_tag():
    """Handle the data for create-a-tag"""
    tag = Tag(name=request.form['name'])

    db.session.add(tag)
    db.session.commit()

    return redirect('/tags')

@app.route('/tags/<int:tag_id>')
def show_tag_details(tag_id):
    """Show a specific tag details & it's posts with the tag related to it"""
    tag = Tag.query.get_or_404(tag_id)

    return render_template('tag-details.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit', methods=['POST'])
def handle_edit_tag_form(tag_id):
    """Handle the data from the tag being edited"""

    return redirect('/')

@app.route('/tags/<int:tag_id>/edit')
def show_edit_tag_form(tag_id):
    """Show the edit tag form"""
    tag = Tag.query.get_or_404(tag_id)
    
    return render_template('edit-tag.html', tag=tag)

@app.route('/tags/<int:tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):
    """Handle the request for deleting a tag"""
    tag = Tag.query.get_or_404(tag_id)

    db.session.delete(tag)
    db.session.commit()

    return redirect('/tags')

# Error for invalid page
@app.errorhandler(404)
def page_error(e):
    """Show 404 page not found"""

    return render_template('404.html')
