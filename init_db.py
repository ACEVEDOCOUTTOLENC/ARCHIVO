from app import create_app, db

# Crear la aplicación Flask
app = create_app()

# Crear todas las tablas definidas en los modelos
with app.app_context():
    db.create_all()
    print("Tablas creadas exitosamente")
