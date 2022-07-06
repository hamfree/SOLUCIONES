from ClasePerson import Persona
class Empleado(Persona):
	def __init__(self, nombre, apellido, peso, altura, salario, experiencia):
		Persona.__init__(self, nombre, apellido, peso, altura)
		self.salario=salario
		self.experiencia=experiencia


	def incremento (self):
		incremento=(self.salario*self.experiencia)/100
		return (incremento)



nombre=raw_input ('Ingrese el nombre: ')
apellido=raw_input ('Ingrese el apellido: ')
peso=float (raw_input ('Ingrese el peso: '))
altura=float (raw_input ('Ingrese la altura: '))
salario=float (raw_input('Ingrese el salario '))
experiencia=float(raw_input('Ingrese los anos trabajados '))

empleado=Empleado(nombre, apellido, peso, altura, salario, experiencia)

print empleado.imc()
print "El incremento correspondiente es: " + str(empleado.incremento()) 

