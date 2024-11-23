from flask import Blueprint, request, jsonify
from entidades.autor import Autor

autor_bp = Blueprint('autores', __name__)

autores = []

@autor_bp.route('/autores', methods=['GET'])
def obtener_autores():
    return jsonify([autor.__dict__ for autor in autores])

@autor_bp.route('/autores', methods=['POST'])
def agregar_autor():
    data = request.json
    autor = Autor(id=data['id'], nombre=data['nombre'])
    autores.append(autor)
    return jsonify(autor.__dict__), 201

@autor_bp.route('/autores/<int:id>', methods=['PUT'])
def editar_autor(id):
    data = request.json
    autor = next((autor for autor in autores if autor.id == id), None)
    if autor:
        autor.nombre = data.get('nombre', autor.nombre)
        autor.fecha_actualizacion = datetime.now()
        return jsonify(autor.__dict__)
    return jsonify({'error': 'Autor no encontrado'}), 404

@autor_bp.route('/autores/<int:id>', methods=['DELETE'])
def eliminar_autor(id):
    global autores
    autores = [autor for autor in autores if autor.id != id]
    return '', 204
