from datetime import datetime

class Autor:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = datetime.now()
        self.fecha_actualizacion = datetime.now()