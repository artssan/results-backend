from Repositories.RepositorioMesas import RepositorioMesas
from Models.Mesas import Mesas

class ControllerMesas():
	
	# Creamos una instancia del repositorio para manejar sus métodos
	def __init__(self):
		self.repositorioMesas = RepositorioMesas()

	# Método índice, usado para listar todos los registros
	def index(self):
		return self.repositorioMesas.findAll()

	# Método crear, usado para crear una nueva mesa
		# Recibe un objeto con los datos de la mesa
	def create(self, infoMesa):
		newMesa = Mesas(infoMesa)
		return self.repositorioMesas.save(newMesa)

	# Método mostrar, usado para mostrar la mesa asociada a la ID recibida
		# Recibe la ID de la mesa y retorna el objeto asociado
	def show(self, id):
		showMesa = Mesas(self.repositorioMesas.findById(id))
		return showMesa.__dict__

	# Método actualizar, usado para actualizar un registro creado anteriormente
		# Recibe la ID del registro y los nuevos datos		
	def update(self, id, infoMesa):
		mesaActual = Mesas(self.repositorioMesas.findById(id))
		mesaActual.cedulas = infoMesa["cedulas"]
		mesaActual.votos = infoMesa["votos"]
		return this.repositorioMesas.save(mesaActual)

	# Método eliminar, usado para eliminar un registro por su ID
		# Recibe la ID de la mesa a eliminar
	def delete(self, id):
		return this.repositorioMesas.delete(id)

	# Método agregar voto a mesa, usado para agregar un voto a la mesa seleccionada
		# Recibe la ID de la mesa en la cual se acaba de realizar un voto, sirve para llevar el conteo
	def addVoteToMesa(self, id):
		mesaActual = Mesas(self.repositorioMesas.findById(id))
		mesaActual.votos += 1
		return this.repositorioMesas.save(mesaActual)