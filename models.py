from flask_sqlalchemy import SQLAlchemy

# Create a database instance
db = SQLAlchemy()

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    username = db.Column(db.String(80), nullable=False, unique=True)  # Unique username
    email = db.Column(db.String(120), nullable=False, unique=True)    # Unique email

    def __repr__(self):
        return f'<User {self.username}>'
