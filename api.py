
from flask import Flask
from routes import Routes
from flask_restful import Resource, Api
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from db_config.database import db
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

jwt = JWTManager(app)


def setup_jwt():
    app.config["JWT_SECRET_KEY"] = "abcde"  # Change this!
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    

def setup_db():
    # 'postgresql://postgres:admin123@localhost:5432/rugged'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin123@localhost:5432/dbtask2'
        # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASESTRING"]
        # print(f'{os.environ["DATABASESTRING"]}')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # app.config['SQLALCHEMY_POOL_SIZE'] = 100
        app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
            'pool_size': 0,
            'pool_recycle': 120,
            'max_overflow': -1,
            'pool_pre_ping': True
        }
        db.init_app(app)
        migrate = Migrate(app, db)
        
print('__name__ is {0}'.format(__name__))
if __name__ in ['__main__', 'api']:
    print("in main")
    setup_jwt()
    setup_db()
    with app.app_context():
        db.create_all()
    route = Routes(app=app, base_path='/api/v1')
    app.run(debug=True)
