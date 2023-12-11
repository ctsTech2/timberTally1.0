import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_APP_SECRET_KEY')

# Use SQLite for this example, replace with your actual database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lumberdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Add the SQLALCHEMY_ECHO setting
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

# Import your models here
from models import Measurement

# Create the database tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

# Import routes after 'app' is defined
import routes