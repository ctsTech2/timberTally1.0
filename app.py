import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # If you're planning to use SQLAlchemy

print(f"Secret Key: {app.config['SECRET_KEY']}")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_APP_SECRET_KEY')  # Load secret key from environment variable

# SQLAlchemy Configuration (if you're using it)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import routes
import routes

if __name__ == "__main__":
    app.run(debug=True)