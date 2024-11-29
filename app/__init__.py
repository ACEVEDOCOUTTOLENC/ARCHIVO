from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializamos SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Usar la configuración definida en config.py

    db.init_app(app)  # Inicializamos la base de datos con la aplicación

    # Importamos las rutas dentro del contexto de la app
    with app.app_context():
        from . import routes, models
        db.create_all()  # Crear las tablas definidas en los modelos al iniciar

    return app
