from models import db
from flask import Flask

app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mboa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de SQLAlchemy
db.init_app(app)

# Création automatique de la base au démarrage
with app.app_context():
    db.create_all()

# Route d'accueil
@app.route('/')
def hello_world():
    return 'Hello, World! This is my first Flask app.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
