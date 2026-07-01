import os
import sys

# Windows ke liye folder structure ka rasta (path) automatic set karne ke liye
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from config import Config
from database.database import db
from routes.home import home_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize extensions
    db.init_app(app)
    
    # Register Modular Blueprints
    app.register_blueprint(home_bp)
    
    with app.app_context():
        db.create_all()  # Generates app.db inside instance/ automatically
        
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)