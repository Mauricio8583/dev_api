from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {"Nome": "Mauricio", "Habilidades": ["Javascript", "Python", "PHP"]},
    {"Nome": "Jonh Doe", "Habilidades": ["Javascript", "Python"]},
    {"Nome": "Jane Doe", "Habilidades": ["Java", "Python"]},    
]

class Desenvolvedor(Resource):
    def get(self, id):
        response = desenvolvedores[id]
        return response
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self, id):
        desenvolvedores.pop(id)
        return {"Status": "Sucesso", "Mensagem": "Registro Excluido"}

class Lista_desenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]



api.add_resource(Desenvolvedor, "/dev/<int:id>/")
api.add_resource(Lista_desenvolvedores, "/dev/")
api.add_resource(Habilidades, "/dev/habilidades")

if __name__ == "__main__":
    app.run(debug=True)