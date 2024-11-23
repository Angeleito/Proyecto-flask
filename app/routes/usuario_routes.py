from flask import Blueprint, request, jsonify
from datetime import datetime
from entidades.usuario import Usuario

usuario_bp = Blueprint('users', __name__)

usuarios = []

@usuario_bp.route('/usuario', methods=['GET'])
def obtener_usuarios():
    return jsonify([usuario.__dict__ for usuario in usuarios])

@usuario_bp.route('/usuario', methods=['POST'])
def agregar_usuario():
    data = request.json
    usuario = Usuario(id=data['id'], nombre=data['nombre'])
    usuarios.append(usuario)
    return jsonify(usuario.__dict__), 201

@usuario_bp.route('/usuario/<int:id>', methods=['PUT'])
def editar_usuario(id):
    data = request.json
    usuario = next((usuario for usuario in usuarios if usuario.id == id), None)
    if usuario:
        usuario.nombre = data.get('nombre', usuario.nombre)
        usuario.fecha_actualizacion = datetime.now()
        return jsonify(usuario.__dict__)
    return jsonify({'error': 'Usuario no encontrado'}), 404

@usuario_bp.route('/usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario.id != id]
    return '', 204
