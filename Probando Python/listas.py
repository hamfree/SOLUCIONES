lista1 = ['manzana',True,'platano','sandia','melocoton','papaya']
lista2 = ['manzana',[1,2,3,4,5,6,7],'C','23.48']

def recorrerLista(lista):                       #procedimiento para recorrer una tupla
	for elemento in lista:                      #mediante el for recorre cada elemento de la tupla
		if  type(elemento) == list: 
			for elemento2 in elemento:           # si dentro de la tupla hay una tupla recorremos la interiro
				print 'elemento ' + str(lista.index(elemento)) +'.' + str(elemento.index(elemento2))+ ': ' + str(elemento2)
		else:                                   # si no imprimimos lo que encontramos
			print 'elemento ' +str(lista.index(elemento)) + ': ' + elemento
			

recorrerLista(lista1)
recorrerLista(lista2)

#acceder a un elemento de la tupla

print 'cuarto elemento de la tupla: '+lista1[3]

#acceder a un elemento de la tupla dentro de la tupla

print 'elemento 2 de la tupla y dentro de esta muestra el cuarto elemento: '+ str(lista2[1][3])

#METODOS LISTAS
#aniadir elemento al final de una lista

lista1.append('tomate')
recorrerLista(lista1)
print ''
lista1.insert(3,'melocoton')
recorrerLista(lista1)
print ''

lista2 [1][3] = 'ahora no es un 4'
recorrerLista(lista2);
print ''
print lista1