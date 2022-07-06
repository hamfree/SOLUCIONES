#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pylint: disable=E1601
#
# Se abre un fichero en modo escritura y se le añaden varias líneas generadas por la cadena
# "Hola" y un número de la lista [5,5,4,5,0,8] en cada línea.
#
def sobreescribirFichero():
	fw = open('fichero2.txt','a')
	for i in [5,5,4,5,0,8]:
		fw.write('Hola'+str(i)+'\n')
	fw.close()

# inicio del programa
sobreescribirFichero()