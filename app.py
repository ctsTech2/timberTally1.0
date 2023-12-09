import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_APP_SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)

# Import routes after 'app' is defined
import routes