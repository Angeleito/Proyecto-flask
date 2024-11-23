from flask import Blueprint, request, jsonify
from entidades.editorial import Editorial

editorial_bp = Blueprint('editoriales', __name__)

editoriales = []

@editorial_bp.route('/', methods=['GET'])
def obtener_editoriales():
    return jsonify([editorial.__dict__ for editorial in editoriales])

@editorial_bp.route('/', methods=['POST'])
def agregar_editorial():
    data = request.json
    editorial = Editorial(id=data['id'], nombre=data['nombre'])
    editoriales.append(editorial)
    return jsonify(editorial.__dict__), 201

@editorial_bp.route('/<int:id>', methods=['PUT'])
def editar_editorial(id):
    data = request.json
    editorial = next((editorial for editorial in editoriales if editorial.id == id), None)
    if editorial:
        editorial.nombre = data.get('nombre', editorial.nombre)
        editorial.fecha_actualizacion = datetime.now()
        return jsonify(editorial.__dict__)
    return jsonify({'error': 'Editorial no encontrada'}), 404

@editorial_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_editorial(id):
    global editoriales
    editoriales = [editorial for editorial in editoriales if editorial.id != id]
    return '', 204
