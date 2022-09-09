from Routes.InterfaceRoutes import InterfaceRoutes
from Controllers.ControllerMesas import ControllerMesas
controladorMesas = ControllerMesas()

class RoutesMesas(InterfaceRoutes(controladorMesas)):
	
	# Ruta para el addVoteToMesa
	def addVote(id):
		json = controladorMesas.addVoteToMesa(id)
		return jsonify(json)