from flask import Flask

def create_app():
    # Create an instance of the Flask class
    app = Flask(__name__)
    
    # Load configuration settings
    # if any

    # Blueprints allow you to organize your application into modules
    from app.main import main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app