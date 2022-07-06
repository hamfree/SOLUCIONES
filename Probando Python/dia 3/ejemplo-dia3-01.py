#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pylint: disable=E1601
"""
Ejemplo 1 de día 3
------------------

Ejemplo de cómo definir una clase y cómo usarla después.
"""

# definición de la clase Saludo
class Saludo(object):
    def __init__(self, nombre,apellido):
            self.nombre = nombre
            self.apellido = apellido
    
    def saludar(self):
        print "Hola, soy ", self.nombre, self.apellido

# inicio del programa

nombre = raw_input('Nombre... :')
apellido = raw_input('Apellido..:')
objeto = Saludo(nombre,apellido)
objeto.saludar()