
personas={}
def leerFicheroADiccionario():
	lineaPersona = 0
	datosPersona = []
	primeraPersona = True
	fr = open('DatosPersonas2.txt','r')
	for linea in fr:
		if primeraPersona:
			datosPersona.insert(lineaPersona,linea)
		else:
			datosPersona[lineaPersona]=linea

		lineaPersona += 1
		if lineaPersona == 5:
			lineaPersona = 0
			persona={}
			persona['Nombre'] = datosPersona[0]
			persona['Apellido1'] = datosPersona[1]
			persona['Apellido2'] = datosPersona[2]
			persona['Edad'] = datosPersona[3]
			personas[datosPersona[4]] = persona
			primeraPersona = False
	fr.close()
			
#-------------------------------------------------------------------------------------------------------------------------------
def mostrarPersonas():
	for persona in personas:
		print personas[persona]["Nombre"]
		print personas[persona]["Apellido1"]
		print personas[persona]["Apellido2"]
		print personas[persona]["Edad"]
		print persona

#-------------------------------------------------------------------------------------------------------------------------------
def escribirDiccionarioFichero():
	fw = open('DatosPersonasRespuesta2.txt','w')
	for persona in personas:
		fw.write('DNI : ' + persona)
		fw.write('Nombre : ' + personas[persona]['Nombre'])
		fw.write( 'Apellido : ' + personas[persona]['Apellido1'])
		fw.write( 'Apellido : ' + personas[persona]['Apellido2'])
		fw.write( 'Edad : ' + personas[persona]['Edad'])
		

#-------------------------------------------------------------------------------------------------------------------------------
leerFicheroADiccionario()
mostrarPersonas()
escribirDiccionarioFichero()