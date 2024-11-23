from flask import Blueprint, request, jsonify
from entidades.libro import Libro

libro_bp = Blueprint('libros', __name__)

libros = []

@libro_bp.route('/', methods=['GET'])
def obtener_libros():
    return jsonify([libro.__dict__ for libro in libros])

@libro_bp.route('/', methods=['POST'])
def agregar_libro():
    data = request.json
    libro = Libro(id=data['id'], nombre=data['nombre'], autor_id=data['autor_id'], genero_id=data['genero_id'])
    libros.append(libro)
    return jsonify(libro.__dict__), 201

@libro_bp.route('/<int:id>', methods=['PUT'])
def editar_libro(id):
    data = request.json
    libro = next((libro for libro in libros if libro.id == id)), None