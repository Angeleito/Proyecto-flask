from datetime import datetime

class Libro:
    def __init__(self, id, nombre, autor_id, genero_id):
        self.id = id
        self.nombre = nombre
        self.autor_id = autor_id
        self.genero_id = genero_id
        self.fecha_creacion = datetime.now()
        self.fecha_actualizacion = datetime.now()