from db_config.database import *
from flask import Flask
from routes import Routes
from flask_cors import CORS
from datetime import timedelta
from modules.course.courseDAO import CourseModel
from modules.student.studentDAO import StudentModel
from modules.user.userDAO import UserModel
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app)
    jwt = JWTManager(app)

    # Configurations
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/swara_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.config["JWT_SECRET_KEY"] = "abcde"  # Change this!
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    
    db.init_app(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
            try:
                db.create_all()
                print("Tables created successfully!")
            except Exception as e:
                print(f"Error creating tables: {e}")
    route = Routes(app=app, base_path='/api/v1')
    app.run(debug=True)