import json

leer = json.loads(open('datos.json').read())
print "los datos de json son \n --------------------------------------\n" + str(leer) + "\n --------------------------------------\n"

print 'El tipo de leer es: '+ str(type(leer))
print 'la lista esta formada por: ' + str(type(leer[0]))
i=0
while i < len(leer):
	print 'El id del elemento'+str(i+1)+' es: '+ str(leer[i]['_id'])
	i += 1

