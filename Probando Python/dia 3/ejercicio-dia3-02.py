#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pylint: disable=E1601
"""
Ejercicio 2 del día 3
---------------------

Programa una clase Empleado que hereda de Persona, de cada empleado debemos 
almacenar salario, años de experiencia y puesto, 
además de los datos de persona.

Debe tener un método que calcule un incremento de salario en base a los años 
de experiencia (1% 1 año de experiencia, 2% 2 años, ...)

"""


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print "Hola, soy ", self.nombre, self.apellido

    def __delete__(self,instance):
        print "...llama al destructor..."

# La clase Empleado hereda de la clase Persona
class Empleado(Persona):
    def __init__(self, nombre, apellido, salario, anualidad, puesto):
        Persona.__init__(self, nombre, apellido)
        self.salario = salario
        self.anualidad = anualidad
        self.puesto = puesto

    def calculaIncremento(self):
        incremento = ((self.anualidad *0.01) * self.salario)
        return incremento

def muestraEmpleado(empleado):
    print "\n\nREGISTRO DEL EMPLEADO"
    print "Nombre................:", empleado.nombre
    print "Apellido..............:", empleado.apellido
    print "Salario...............:", empleado.salario
    print "Años de experiencia...:", empleado.anualidad
    print "Puesto................:", empleado.puesto
    print "\n"

def creaEmpleado():
    nombre =        raw_input('Nombre...............:')
    apellido =      raw_input('Apellido.............:')
    salario =   int(raw_input('Salario..............:'))
    anualidad = int(raw_input('anualidad de experiencia..:'))
    puesto =        raw_input('Puesto...............:')    
    empleado = Empleado(nombre,apellido,salario,anualidad,puesto)
    return empleado

# Inicio del programa


miEmpleado = creaEmpleado()
salarioCalculado = miEmpleado.calculaIncremento()
muestraEmpleado(miEmpleado)
print "\n\nIncremento de salario...:", salarioCalculado
