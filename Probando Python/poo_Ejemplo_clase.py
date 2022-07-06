class Saludo(object):
	def __init__(self, nombre,apellido):
		self.nombre = nombre
		self.apellido = apellido

	def saludar(self):
		print "Hola soy", self.nombre, self.apellido
		
	def __delete__(self):
		print "Llamada al destructor"
	

	
nombre = raw_input('Nombre: ')
apellido = raw_input('Apellido: ')
objeto = Saludo(nombre, apellido)
objeto.saludar()
