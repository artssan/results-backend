from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controllers.ControllerMesas import ControllerMesas
from Controllers.ControllerPartidos import ControllerPartidos

app = Flask(__name__)
cors = CORS(app)

controladorMesas = ControllerMesas()
controladorPartido = ControllerPartidos()

# ------------- [[ Rutas de Mesas ]] -------------

@app.route("/mesas", methods = ['GET'])
def getMesas():
	json = controladorMesas.index()
	return jsonify(json)

@app.route("/mesas", methods = ['POST'])
def postMesas():
	data = request.get_json()
	json = controladorMesas.create(data)
	return jsonify(json)

@app.route("/mesas/<string:id>", methods = ['GET'])
def getMesa(id):
	json = controladorMesas.show(id)
	return jsonify(json)

@app.route("/mesas/<string:id>", methods = ['PUT'])
def putMesas(id):
	data = request.get_json()
	json = controladorMesas.update(id,data)
	return jsonify(json)

@app.route("/mesas/<string:id>", methods = ['DELETE'])
def deleteMesas(id):
	json = controladorMesas.delete(id)
	return jsonify(json)

@app.route("/mesas/<string:id>", methods = ['POST'])
def postVote(id):
	json = controladorMesas.addVoteToMesa(id)
	return jsonify(json)

# ------------- [[ Rutas de Partidos ]] -------------
@app.route("/partido", methods = ['GET'])
def getPartido():
	json = controladorPartido.index()
	return jsonify(json)

@app.route("/partido", methods = ['POST'])
def postPartido():
	data = request.get_json()
	json = controladorPartido.create(data)
	return jsonify(json)

@app.route("/partido/<string:id>", methods = ['GET'])
def getPartido(id):
	json = controladorPartido.show(id)
	return jsonify(json)

@app.route("/partido/<string:id>", methods = ['PUT'])
def putPartido(id):
	data = request.get_json()
	json = controladorPartido.update(id,data)
	return jsonify(json)

@app.route("/partido/<string:id>", methods = ['DELETE'])
def deletePartido(id):
	json = controladorPartido.delete(id)
	return jsonify(json)




# Función para cargar el archivo config del server
def loadFileConfig():
	with open('config.json') as f:
		data = json.load(f)
	return data

# Iniciador del server, con un print para identificar el correcto funcionamiento
if __name__ == "__main__":
	dataConfig = loadFileConfig()
	print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
	serve(app, host = dataConfig["url-backend"], port = dataConfig["port"])