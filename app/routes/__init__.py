from .autor_routes import autor_bp
from .editorial_routes import editorial_bp
from .genero_routes import genero_bp
from .libro_routes import libro_bp
from .resena_routes import resena_bp
from .usuario_routes import usuario_bp

def registrar_rutas(app):
    app.register_blueprint(autor_bp, url_prefix='/autores')
    app.register_blueprint(editorial_bp, url_prefix='/editoriales')
    app.register_blueprint(genero_bp, url_prefix='/generos')
    app.register_blueprint(libro_bp, url_prefix='/libros')
    app.register_blueprint(resena_bp, url_prefix='/resenas')
    app.register_blueprint(usuario_bp, url_prefix='/usuarios')