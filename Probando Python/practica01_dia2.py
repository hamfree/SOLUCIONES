#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pylint: disable=E1601
"""
Por equipos de 2 personas, leer un fichero con datos de 3 personas, cada dato en una línea y pasarlo a 
un diccionario.

Realizar también el paso inverso, de diccionario volver a escribir en un segundo fichero.

"""
dic = {}
fichero=open('persona2.txt','r')
for linea in fichero:
        persona=linea.split('$')
        personasinnombre=[persona[1],persona[2],persona[3]]
        dic[persona[0]] = personasinnombre 
print dic