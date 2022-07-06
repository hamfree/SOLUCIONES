class FicherosDeEmpleados(object):
	def __init__(self,empleados):
		self.empleados = empleados
		self.fw = open("ficheroEscribir.txt","w")
		self.fr = open("ficheroLeer.txt","r")

	def pedirEmpleados(self):
		persona={}
		persona["nombre"] = raw_input ("Inserte su nombre: ")
		persona["apellido"]= raw_input ("Inserte su primer apellido: ")
		persona["peso"]= raw_input ("Ingrese el peso: ")
		persona["altura"] = int(raw_input ("Ingrese la altura: "))
		persona["salario"]= raw_input ("Ingrese el salario: ")
		persona["experiencia"] = int(raw_input ("Ingrese la experiencia: "))
		self.empleados.append(persona)

	def pasarAFichero(self):
		for empleado in self.empleados:
			self.fw.write("-------------------------------------------------------\n")
			self.fw.write("nombre : " + empleado["nombre"] + "\n")
			self.fw.write("apellido : " + empleado["apellido"]+ "\n")
			self.fw.write("peso : " + str(empleado["peso"])+ "\n")
			self.fw.write("altura : " + str(empleado["altura"])+ "\n")
			self.fw.write("salario : " + str(empleado["salario"])+ "\n")
			self.fw.write("experiencia : " + str(empleado["experiencia"])+ "\n")
			self.fw.write("-------------------------------------------------------\n")
	def leerListaDeFichero(self):
		contLineas = 0
		datosempleado=[]
		for linea in self.fr:
			datosempleado.insert(contLineas,linea)
			if contLineas < 5:
				contLineas += 1
			else:
				empleado={}
				empleado["nombre"] = datosempleado[0] 
				empleado["apellido"] = datosempleado[1]
				empleado["peso"] = datosempleado[2]
				empleado["altura"] = datosempleado[3] 
				empleado["salario"] = datosempleado[4]
				empleado["experiencia"]=datosempleado[5] 
				self.empleados.append(empleado)
				contLineas = 0
	def mostrarEmpleados(self):
		for empleado in self.empleados:
			print "-------------------------------------------------------\n"
			print "nombre : " + empleado["nombre"] + "\n"
			print "apellido : " + empleado["apellido"]+ "\n"
			print "peso : " + str(empleado["peso"])+ "\n"
			print "altura : " + str(empleado["altura"])+ "\n"
			print "salario : " + str(empleado["salario"])+ "\n"
			print "experiencia : " + str(empleado["experiencia"])+ "\n"
			print"-------------------------------------------------------\n"

	  	def __delete__(self):
	  		self.fr.close()
	  		self.fw.close()

empleados = []
fichero = FicherosDeEmpleados(empleados)
fichero.leerListaDeFichero()
fichero.mostrarEmpleados()
fichero.pasarAFichero()
fichero.__delete__()