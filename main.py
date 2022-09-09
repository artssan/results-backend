from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Routes.RoutesMesas import RoutesMesas

app = Flask(__name__)
cors = CORS(app)

rutasMesa = RoutesMesas()

# ------------- [[ Rutas de Mesas ]] -------------

@app.route("/mesas", methods = ['GET'])
rutasMesa.getAll()

@app.route("/mesas", methods = ['POST'])
rutasMesa.create(request.get_json())

@app.route("/mesas/<string:id>", methods = ['GET'])
rutasMesa.get(id)

@app.route("/mesas/<string:id>", methods = ['PUT'])
rutasMesa.update(id, request.get_json())

@app.route("/mesas/<string:id>", methods = ['DELETE'])
rutasMesa.delete(id)

@app.route("/mesas/<string:id>", methods = ['POST'])
rutasMesa.addVote(id)

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