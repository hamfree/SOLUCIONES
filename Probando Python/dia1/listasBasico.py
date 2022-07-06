
lista = ['manzana',[1,2,3,4,5,6,7],'C','23.48']


#acceder a un elemento de la tupla

print 'cuarto elemento de la lista: '+lista[3]

#acceder a un elemento de la tupla dentro de la tupla

print 'elemento 2 de la lista y dentro de esta muestra el cuarto elemento: '+ str(lista[1][3])

#METODOS LISTAS
#aniadir elemento al final de una lista
print ''
print 'Introducimos tomate al final de la lista "append()"'
lista.append('tomate')
print lista
print ''
print 'Introducimos melocoton en la posicion 3  de la lista "insert(3,"melocoton")"'
lista.insert(3,'melocoton')
print lista
print ''
print 'accedemos a la posicion de la lista 2 donde hay una lista y aqui a la posicion 4 y lo cambiamos por "ahora no es un 4"'
lista [1][3] = 'ahora no es un 4'
print ''
print lista