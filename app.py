from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

desenvolvedores = [
    {"Nome": "Mauricio", "Habilidades": ["Javascript", "Python", "PHP"]},
    {"Nome": "Jonh Doe", "Habilidades": ["Javascript", "Python"]},
    {"Nome": "Jane Doe", "Habilidades": ["Java", "Python"]},    
]

@app.route("/dev/<int:id>/", methods=["GET", "PUT", "DELETE"])
def devs(id):
    if request.method == "GET":
        dev = desenvolvedores[id]
        return jsonify(dev)
    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({"Status": "Excluido", "Mensagem": "Registro excluido"})

@app.route("/dev/", methods=["GET", "POST"])
def lista_dev():
    if request.method == "POST":
        dados = request.data
        desenvolvedores.append(dados)
        return jsonify({"Status": "Sucess", "Mensagem": "Novo registro incluido"})
    elif request.method == "GET":
        return jsonify(desenvolvedores)


if __name__ == "__main__":
    app.run(debug=True)

