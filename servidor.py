from flask import Flask, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'clave-secreta'  # Reemplazar por algo más seguro en producción
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

# Modelo Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contrasena = db.Column(db.String(200), nullable=False)

# Crear DB
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('tareas'))

# Registro de usuario
@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')

    if Usuario.query.filter_by(usuario=usuario).first():
        return jsonify({"error": "Usuario ya existe"}), 400

    contrasena_hash = generate_password_hash(contrasena)
    nuevo_usuario = Usuario(usuario=usuario, contrasena=contrasena_hash)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

# Login
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')

    usuario_db = Usuario.query.filter_by(usuario=usuario).first()

    if usuario_db and check_password_hash(usuario_db.contrasena, contrasena):
        session['usuario'] = usuario
        return jsonify({"mensaje": "Inicio de sesión exitoso"}), 200
    return jsonify({"error": "Credenciales inválidas"}), 401

# Tareas (HTML)
@app.route('/tareas', methods=['GET'])
def tareas():
    if 'usuario' not in session:
        return jsonify({"error": "No autenticado"}), 401
    return f'''
    <html>
    <head><title>Bienvenido</title></head>
    <body>
        <h1>¡Bienvenido, {session["usuario"]}!</h1>
        <p>Has iniciado sesión correctamente.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
