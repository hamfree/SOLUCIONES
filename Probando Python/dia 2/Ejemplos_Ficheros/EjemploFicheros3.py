#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pylint: disable=E1601
#
# Abre el fichero 'fichero.txt' en modo lectura y lo copia línea a línea en uno nuevo (o lo sobreescribe 
# si existe) llamado 'fichero3.txt' anteponiendo en cada línea del nuevo fichero el texto:
# 'linea escrita desde script_____: '
#
def leerEscribirFichero():

	fr = open('fichero.txt','r')
	fw = open('fichero3.txt','w')
	for linea in fr:
		fw.write('linea escrita desde script_____: ')
		fw.write(linea+ '\n')
	fr.close()
	fw.close()
	
# inicio del programa
leerEscribirFichero()