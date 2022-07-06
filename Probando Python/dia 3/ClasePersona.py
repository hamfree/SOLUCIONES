class Persona (object):
	"""docstring for Persona """
	def __init__(self, nombre, apellido, peso, altura):
		self.nombre = nombre
		self.apellido = apellido
		self.peso = peso
		self.altura = altura

	def imc (self):
		indice=self.peso/(self.altura*self.altura)
		if indice<18:
			return "Peso bajo"
		else:
			if indice>=18 and indice<25:
				return "Peso normal"
			else:
				return "Peso alto"

"""

nombre=raw_input ('Ingrese el nombre: ')
apellido=raw_input ('Ingrese el apellido: ')
peso=float (raw_input ('Ingrese el peso: '))
altura=float (raw_input ('Ingrese la altura: '))

persona=Persona(nombre, apellido, peso, altura)
print "La persona "+nombre+" tiene un: "        
persona.imc() """



