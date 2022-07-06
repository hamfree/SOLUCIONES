#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pylint: disable=E1601
"""
    Práctica 01 del día 3.
    ----------------------

    Crea una clase Ficheros, que lea una lista de diccionarios de Empleados y los pase a fichero y 
    que también haga el paso inverso, de fichero a lista de diccionarios.
"""

# La clase Persona representa a una persona
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

# La nueva clase a realizar...
class Ficheros(object):
    def __init__(self,nombre,listaEmpleados):
        self.nombre = nombre
        self.listaEmpleados = listaEmpleados

    def __delete__(self,instance):
        print "...llama al destructor..."

    def exportaEmpleados(self):
        fw = open(self.nombre,'a')
        for elemento in self.listaEmpleados:
            fw.write(str(elemento))
        fw.close()        

    def importaEmpleados(self):
        fr = open(self.nombre,'r')

        pass    


def creaUnaListaDeTrabajadores():
    print "Creamos un diccionario de empleados...."
    empleados = {}
    emp1 = Empleado('Juan Francisco','Ruiz',18300,6,'Programador')
    empleados[emp1.nombre] = emp1
    emp2 = Empleado('Pedro','Barea',42000,15,'Analista')
    empleados[emp2.nombre] = emp2
    emp3 = Empleado('Ana','Torroja',34000,9,'Jefe de proyecto')
    empleados[emp3.nombre] = emp3
    return empleados

def muestraEmpleado(empleado):
    print "\n\nREGISTRO DEL EMPLEADO"
    print "Nombre................:", empleado.nombre
    print "Apellido..............:", empleado.apellido
    print "Salario...............:", empleado.salario
    print "Años de experiencia...:", empleado.anualidad
    print "Puesto................:", empleado.puesto
    print "\n"

def muestraDicEmpleados(dic):
    for empleado in dic:
        muestraEmpleado(empleado)
        print "\n"


# -------------------------------- inicio del programa -----------------------------------
listaEmpleados = creaUnaListaDeTrabajadores()
misFicheros = Ficheros('misEmpleados.txt',listaEmpleados)
print "Exportamos el diccionario de empleados al fichero 'misEmpleados.txt'"
misFicheros.exportaEmpleados()

dicTrabajadores = {}
otrosFicheros = Ficheros('misEmpleados.txt',dicTrabajadores)

print "Importamos un diccionario de empleados desde el fichero 'misEmpleados.txt'"
otrosFicheros.importaEmpleados()

print "Lo mostramos en pantalla...."
muestraDicEmpleados(otrosFicheros)
