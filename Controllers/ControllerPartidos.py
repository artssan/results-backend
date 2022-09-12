from Repositories.RepositorioPartidos import RepositorioPartidos
from Models.Partidos import Partidos

class ControllerPartidos():
	
	def __init__(self):
		self.RepositorioPartidos = RepositorioPartidos()

	def index(self):
		return self.RepositorioPartidos.findAll()

	def create(self, inforPartidos):
		part = Partidos(inforPartidos)
		return self.RepositorioPartidos.save(part)

	def show(self, id):
		par = Partidos(self.RepositorioPartidos.findById(id))
		return par.__dict__

	def update(self, id, infoMesa):
		par = Partidos(self.RepositorioPartidos.findById(id))
		par.nombre = infoMesa["nombre"]
		par.lema = infoMesa["lema"]
		return self.RepositorioPartidos.save(par)

	def delete(self, id):
		return self.RepositorioPartidos.delete(id)

