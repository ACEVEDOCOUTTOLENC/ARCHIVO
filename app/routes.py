from app import db
from flask import render_template
from app import create_app

# Definir rutas aquí, sin necesidad de importar app directamente
app = create_app()

@app.route('/')
def index():
    return "¡Conexión exitosa a la base de datos!"
