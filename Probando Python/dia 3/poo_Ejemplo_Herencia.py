class Saludo(object):
	def __init__(self, nombre,apellido):
		self.nombre = nombre
		self.apellido = apellido

	def saludar(self):
		print "Hola soy", self.nombre, self.apellido
		
	def __delete__(self):
		print "Llamada al destructor"
	
class Saludo2(Saludo):
	def __init__(self, nombre,apellido, edad):
		Saludo.__init__(self, nombre, apellido)
		self.edad = edad;
	def saludar(self):
		Saludo.saludar(self)
		print "Edad: ", self.edad
	
nombre = raw_input('Nombre: ')
apellido = raw_input('Apellido: ')
objeto = Saludo(nombre, apellido)
objeto.saludar()
objeto2 = Saludo2(nombre, apellido, 17)
objeto2.saludar()
objeto2.__delete__()