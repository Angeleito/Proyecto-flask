from flask import Flask
from flask_mysqldb import MySQL
from config import config
from routes import registrar_rutas

app = Flask(__name__)
app.config.from_object(config['development'])

mysql = MySQL(app)

registrar_rutas(app)

if __name__ == '__main__':
    app.run()