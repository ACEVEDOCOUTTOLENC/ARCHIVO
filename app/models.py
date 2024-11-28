from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo Usuarios
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, unique=True, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    expedientes = db.relationship('Expediente', backref='usuario', lazy=True)

# Modelo Areas
class Area(db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String, nullable=False)
    expedientes = db.relationship('Expediente', backref='area', lazy=True)

# Modelo Expediente
class Expediente(db.Model):
    __tablename__ = 'expediente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    clave = db.Column(db.String, unique=True, nullable=False)
    ubicacion_id = db.Column(db.String, nullable=False)  # Relación lógica para Ubicación
    acceso = db.Column(db.String, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    status = db.Column(db.String, nullable=False)

# Modelo Salas
class Sala(db.Model):
    __tablename__ = 'salas'
    id = db.Column(db.Integer, primary_key=True)
    sala = db.Column(db.String, nullable=False)
    estantes = db.relationship('Estante', backref='sala', lazy=True)

# Modelo Estantes
class Estante(db.Model):
    __tablename__ = 'estantes'
    id = db.Column(db.Integer, primary_key=True)
    estante = db.Column(db.String, nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey('salas.id'), nullable=False)
    repisas = db.relationship('Repisa', backref='estante', lazy=True)

# Modelo Repisas
class Repisa(db.Model):
    __tablename__ = 'repisas'
    id = db.Column(db.Integer, primary_key=True)
    repisa = db.Column(db.String, nullable=False)
    estante_id = db.Column(db.Integer, db.ForeignKey('estantes.id'), nullable=False)
