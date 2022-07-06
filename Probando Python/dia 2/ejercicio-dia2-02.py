#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pylint: disable=E1601
"""
Crea un diccionario en el que almacenes los datos de varias personas usando el dni como clave y como 
valor, un diccionario etiquetando el resto de datos.

"""

diccionario = {'a':[1,3,5],'b':[2,4,6]}
for (c,v) in diccionario.keys(),diccionario.values():
    print c,v
