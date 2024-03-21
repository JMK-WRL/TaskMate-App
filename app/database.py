from .models.base import db

def init_db(app):
    """
    Initialize the database connection with the Flask app.
    """
    db.init_app(app)

# Define SQLAlchemy models
class User(db.Model):
    """
    SQLAlchemy model for user table.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))  # Increase length for hashed passwords
    # Add more fields as needed

class Task(db.Model):
    """
    SQLAlchemy model for task table.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    description = db.Column(db.String(256))
    due_date = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='tasks')
    # Add more fields as needed
