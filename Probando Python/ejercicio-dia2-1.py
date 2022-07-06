
def agregarPersona(personas,valores):
	personas[valores[4]] = valores[0:4]

def pedirPersona():
	persona=[]
	persona.append(raw_input ("Inserte su nombre "))
	persona.append(raw_input ("Inserte su primer apellido "))
	persona.append(raw_input ("Inserte su segundo apellido "))
	persona.append(int(raw_input ("Inserte su edad ")))
	persona.append(raw_input ("Inserte su dni "))
	return persona
def crearDiccionarioPersonas(numeroPersonas):
	personas={}
	cont = 0
	while cont <numeroPersonas:
		agregarPersona(personas,pedirPersona())
		cont += 1
	return personas
def mostrarPersonas(personas):
	for persona in personas:
		print "--------------------------------------------"
		print "Nombre : " + personas[persona][0]
		print "Primer apellido : " + personas[persona][1]
		print "Segundo apellido : " + personas[persona][2]
		print "edad : " + personas[persona][3]
		print "DNI : " + persona
		print "--------------------------------------------"

mostrarPersonas(crearDiccionarioPersonas(2))
