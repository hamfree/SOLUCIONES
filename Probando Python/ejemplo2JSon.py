import json
def agregarPersona(personas):
	
	personas.append(pedirPersona())

def pedirPersona():
	persona={}
	persona["nombre"] = raw_input ("Inserte su nombre: ")
	persona["apellido1"]= raw_input ("Inserte su primer apellido: ")
	persona["apellido2"]= raw_input ("Inserte su segundo apellido: ")
	persona["edad"] = int(raw_input ("Inserte su edad: "))
	persona["dni"] = raw_input("introduce el DNI : ")
	return persona

def crearListaPersonas(numeroPersonas):
	personas=[]
	cont = 0
	while cont <numeroPersonas:
		print "persona " + str(cont + 1)
		agregarPersona(personas)
		cont += 1
	return personas
def mostrarPersonas(personas):
	for persona in personas:
		print "--------------------------------------------"
		print "Nombre : " + persona["nombre"]
		print "Primer apellido : " + persona["apellido1"]
		print "Segundo apellido : " + persona["apellido2"]
		print "edad : " + str(persona["edad"])
		print "DNI : " + persona["dni"]
		print "--------------------------------------------"
personas = crearListaPersonas(2)
mostrarPersonas(personas)

fr = open('datos2.json', 'w')
json.dump(personas, fr)

