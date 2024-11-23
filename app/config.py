class DevelopmentConfig:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'proyecto_flask'
    DEBUG = True

config = {
    'development': DevelopmentConfig
}