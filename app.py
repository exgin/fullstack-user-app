"""Blogly application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


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