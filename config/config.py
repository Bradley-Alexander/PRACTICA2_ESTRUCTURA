from os import environ, path

base_dir = path.abspath(path.dirname('__file__'))

class Config:
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    

