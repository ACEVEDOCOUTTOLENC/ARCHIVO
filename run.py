from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Inicializar la aplicación Flask
app = Flask(__name__, 
            static_url_path='/static', 
            static_folder='app/static',
            template_folder='app/templates')

# Obtener la URL de la base de datos desde el archivo .env
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Desactivar el seguimiento de modificaciones
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
