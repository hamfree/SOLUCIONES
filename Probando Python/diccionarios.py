diccionario1 = {'str':'esto es un string' , 'char':'C' , 'list':['elemento 1','elemento 2','elemento 3']}

def recorrerDiccionario(diccionario):                       #procedimiento para recorrer una tupla
	for elemento in diccionario:                      #mediante el for recorre cada elemento de la tupla
		if  type(diccionario1[elemento]) == list: 
			for elemento2 in diccionario1[elemento]:           # si dentro de la tupla hay una tupla recorremos la interiro
				print elemento +'.' + str(diccionario1[elemento].index(elemento2))+ ': ' + str(elemento2)
		else:                                   # si no imprimimos lo que encontramos
			print 'elemento '  + ': ' + elemento + ': '+ str(diccionario1[elemento])
			

recorrerDiccionario(diccionario1)

print diccionario1['str']
print diccionario1['char']
print diccionario1['list']

