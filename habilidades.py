from flask_restful import Resource

habilidades_lista = ["Java", "JavaScript", "Python"]

class Habilidades(Resource):
    def get(self):
        return habilidades_lista

