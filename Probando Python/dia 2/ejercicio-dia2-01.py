#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pylint: disable=E1601
"""

Crea un diccionario en el que almacenes los datos de varias personas usando el dni como clave y  como 
valor, una lista con el resto de datos (usa como base el del ejercicio 1)

"""
# Muestra de datos
def muestraPersonas(dpers):
    if len(dpers) > 0:
        print "Personas en el diccionario:" + str(len(dpers))
        claves = dpers.keys()
        for c in claves:
            print "-------------------------------------------------------"
            print "DNI :" + c
            valor = dpers[c]
            for v in valor:
                print v + " : " + str(valor[v])
            print "-------------------------------------------------------"
# Recogida de datos
def recogidaDatos():
    persona = {}
    valido = False
    esNombreValido = False
    esApellidoValido = False
    esEdadValida = False
    esPesoValido = False
    esAlturaValida = False
    while not valido:
        while not esNombreValido:
            entrada = raw_input('Nombre:')
            if len(entrada) > 0:
                persona['nombre'] = entrada
                esNombreValido = True
            else:
                print "El nombre es obligatorio"
        while not esApellidoValido:
            entrada = raw_input('Apellidos:')
            if len(entrada) > 0:
                persona['apellidos'] = entrada
                esApellidoValido = True
            else:
                print "El apellido es obligatorio"
        while not esEdadValida:
            entrada = raw_input('Edad:')
            numero = int(entrada)
            if numero > 0 and numero < 100:
                persona['edad'] = int(entrada)
                esEdadValida = True
            else:
                print "La edad debe estar entre 0 y 100"
        while not esPesoValido:
            entrada = raw_input('Peso:')
            numero = int(entrada)
            if numero > 35 and numero < 125:
                persona['peso'] = int(entrada)
                esPesoValido = True
            else:
                print "El peso debe estar entre 35 y 125"
        while not esAlturaValida:
            entrada = raw_input('Altura:')
            numero = int(entrada)
            if numero > 50 and numero < 250:
                persona['altura'] = int(entrada)
                esAlturaValida = True
                valido = True
            else:
                print "La altura debe estar entre 50 y 250 cm"
        return persona

# valida el dni que se le pasa
def validaDni(dni):
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    dig_ext = "XYZ"
    reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
    numeros = "1234567890"
    dni = dni.upper()
    if len(dni) == 9:
        dig_control = dni[8]
        dni = dni[:8]
        if dni[0] in dig_ext:
            dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
        return len(dni) == len([n for n in dni if n in numeros]) \
            and tabla[int(dni)%23] == dig_control
    return False

# inicio del programa
dpers = {}

print "Ejercicio 1 del dia 2\n"
print "----------------------\n\n"
elUsuarioQuiereSalir = False

while not elUsuarioQuiereSalir:
    dni = raw_input("Dime un DNI (para salir indique 'salir'): ")
    if dni == "salir":
        elUsuarioQuiereSalir = True
        break
    elif len(dni) == 0:
        print "El DNI es obligatorio, tio."
    elif validaDni(dni):
        persona = recogidaDatos()
        if dpers.has_key(dni):
            print "Ya existe una persona con el dni " + dni
        else:
            # se añade, dandole el valor de una clave nueva
           dpers[dni]=persona
    else:
        print "Ese DNI es mas falso que un billete de tres euros... No me engañes..."

if len(dpers) > 0:
    print "El diccionario de personas es:\n"
    # print dpers
    muestraPersonas(dpers)
else:
    print "el diccionario de personas esta vacio\n"
    

print "El usuario se canso de mi... Terminando..."


