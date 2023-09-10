from ClasePersona import Persona
class Empleado(Persona):
	def __init__(self, nombre, apellido, peso, altura, salario, experiencia):
		Persona.__init__(self, nombre, apellido, peso, altura)
		self.salario=salario
		self.experiencia=experiencia
	def incremento (self):
		incremento=(self.salario*self.experiencia)/100
		return (incremento)



nombre=input('Ingrese el nombre: ')
apellido=input('Ingrese el apellido: ')
peso=float (input('Ingrese el peso: '))
altura=float (input('Ingrese la altura: '))
salario=float (input('Ingrese el salario '))
experiencia=float(input('Ingrese los anos trabajados '))

empleado=Empleado(nombre, apellido, peso, altura, salario, experiencia)

print (empleado.imc())
print ("El incremento correspondiente es: " + str(empleado.incremento()))

