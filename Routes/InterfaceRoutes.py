# Clase genérica para heredar en las distintas rutas
class InterfaceRoutes(controller):
	
	# Ruta para el index
	def getAll():
		json = controller.index()
		return jsonify(json)

	# Ruta para el create
	def create(data):
		json = controller.create(data)
		return jsonify(json)

	# Ruta para el show
	def get(id):
		json = controller.show(id)
		return jsonify(json)

	# Ruta para el update
	def update(id, data):
		json = controller.update(id, data)
		return jsonify(json)

	# Ruta para el delete
	def delete(id):
		json = controller.delete(id)
		return jsonify(json)