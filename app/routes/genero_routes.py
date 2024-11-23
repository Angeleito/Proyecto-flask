from flask import Blueprint, request, jsonify
from entidades.genero import Genero

genero_bp = Blueprint('generos', __name__)

generos = []

@genero_bp.route('/', methods=['GET'])
def obtener_generos():
    return jsonify([genero.__dict__ for genero in generos])

@genero_bp.route('/', methods=['POST'])
def agregar_genero():
    data = request.json
    genero = Genero(id=data['id'], nombre=data['nombre'])
    generos.append(genero)
    return jsonify(genero.__dict__), 201

@genero_bp.route('/<int:id>', methods=['PUT'])
def editar_genero(id):
    data = request.json
    genero = next((genero for genero in generos if genero.id == id), None)
    if genero:
        genero.nombre = data.get('nombre', genero.nombre)
        genero.fecha_actualizacion = datetime.now()
        return jsonify(genero.__dict__)
    return jsonify({'error': 'Genero no encontrado'}), 404

@genero_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_genero(id):
    global generos
    generos = [genero for genero in generos if genero.id != id]
    return '', 204
