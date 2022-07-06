tupla1 = ('manzana','naranja','platano','sandia','melocoton','papaya')
tupla2 = ('manzana',(1,2,3,4,5,6,7),'C','23.48')

def recorrerTupla(tupla):                       #procedimiento para recorrer una tupla
	for elemento in tupla:                      #mediante el for recorre cada elemento de la tupla
		if  type(elemento) == tuple: 
			for elemento2 in elemento:           # si dentro de la tupla hay una tupla recorremos la interiro
				print 'elemento ' + str(tupla.index(elemento)) +'.' + str(elemento.index(elemento2))+ ': ' + str(elemento2)
		else:                                   # si no imprimimos lo que encontramos
			print 'elemento ' +str(tupla.index(elemento)) + ': ' + elemento
			

recorrerTupla(tupla1)
recorrerTupla(tupla2)

#acceder a un elemento de la tupla

print 'cuarto elemento de la tupla: '+tupla1[3]

#acceder a un elemento de la tupla dentro de la tupla

print 'elemento 2 de la tupla y dentro de esta muestra el cuarto elemento: '+ str(tupla2[1][3])