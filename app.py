from models import db
from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mboa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database connection
db.init_app(app)

# Automatically create database tables if they don't exist
with app.app_context():
    db.create_all()

# Define a simple route
@app.route('/')
def hello_world():
    return 'Hello, World! This is my first Flask app.'

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
