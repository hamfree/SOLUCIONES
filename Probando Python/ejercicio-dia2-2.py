#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pylint: disable=E1601
def agregarPersona(personas):
	dni = raw_input("introduce el DNI de la persona que desee introducir : ")
	personas[dni] = pedirPersona()

def pedirPersona():
	persona={}
	persona["nombre"] = raw_input ("Inserte su nombre: ")
	persona["apellido1"]= raw_input ("Inserte su primer apellido: ")
	persona["apellido2"]= raw_input ("Inserte su segundo apellido: ")
	persona["edad"] = int(raw_input ("Inserte su edad: "))
	return persona

def crearDiccionarioPersonas(numeroPersonas):
	personas={}
	cont = 0
	while cont <numeroPersonas:
		print "persona " + str(cont + 1)
		agregarPersona(personas)
		cont += 1
	return personas
def mostrarPersonas(personas):
	for persona in personas:
		print "--------------------------------------------"
		print "Nombre : " + personas[persona]["nombre"]
		print "Primer apellido : " + personas[persona]["apellido1"]
		print "Segundo apellido : " + personas[persona]["apellido2"]
		print "edad : " + str(personas[persona]["edad"])
		print "DNI : " + persona
		print "--------------------------------------------"

mostrarPersonas(crearDiccionarioPersonas(2))
