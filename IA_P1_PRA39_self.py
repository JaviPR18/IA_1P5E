class Usuario:
	def __init__(self, nombre, apellidos):
		self.nombre = nombre
	self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Enrique', 'Plascencia Hernández')

usuario002 = Usuario('Javier', 'Plascencia Ramirez')

usuario002.nombre = 'Dana Sofia'

usuario002.imprime_datos()