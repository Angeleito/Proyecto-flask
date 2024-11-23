from flask import Blueprint, request, jsonify
from datetime import datetime
from entidades.resena import Resena

resena_bp = Blueprint('resenas', __name__)

resenas = []

@resena_bp.route('/', methods=['GET'])
def obtener_resenas():
    return jsonify([resena.__dict__ for resena in resenas])

@resena_bp.route('/', methods=['POST'])
def agregar_resena():
    data = request.json
    resena = Resena(id=data['id'], contenido=data['contenido'], libro_id=data['libro_id'], usuario_id=data['usuario_id'])
    resenas.append(resena)
    return jsonify(resena.__dict__), 201

@resena_bp.route('/<int:id>', methods=['PUT'])
def editar_resena(id):
    data = request.json
    resena = next((resena for resena in resenas if resena.id == id), None)
    if resena:
        resena.contenido = data.get('contenido', resena.contenido)
        resena.libro_id = data.get('libro_id', resena.libro_id)
        resena.usuario_id = data.get('usuario_id', resena.usuario_id)
        resena.fecha_actualizacion = datetime.now()
        return jsonify(resena.__dict__)
    return jsonify({'error': 'Reseña no encontrada'}), 404

@resena_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_resena(id):
    global resenas
    resenas = [resena for resena in resenas if resena.id != id]
    return '', 204