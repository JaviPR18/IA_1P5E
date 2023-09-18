class Usuario:
	nombres = ''
	apellidos = ''

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario()

usuario001.nombre = 'Leonel Andres'
usuario001.apellidos = 'Messi Cuccitini'

usuario001.imprime_datos()