from run import app, db  # Importa la aplicación y la base de datos desde run.py
from app.models import Usuario, Area, Expediente, Estante, Repisa  # Importa tus modelos

# Establecer el contexto de la aplicación
with app.app_context():
    # Crear las tablas
    db.create_all()
    print("Tablas creadas exitosamente.")
