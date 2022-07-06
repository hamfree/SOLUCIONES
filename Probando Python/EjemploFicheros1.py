#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pylint: disable=E1601
#
# Se abre un fichero en modo lectura y se muestra línea a línea en la pantalla.
#
def leerFichero():
	fr = open('fichero.txt','r')
	for linea in fr:
		print linea
	fr.close()

# inicio del programa
leerFichero()