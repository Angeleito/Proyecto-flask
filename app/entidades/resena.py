from datetime import datetime

class Resena:
    def __init__(self, id, contenido, libro_id, usuario_id):
        self.id = id
        self.contenido = contenido
        self.libro_id = libro_id
        self.usuario_id = usuario_id
        self.fecha_creacion = datetime.now()
        self.fecha_actualizacion = datetime.now()