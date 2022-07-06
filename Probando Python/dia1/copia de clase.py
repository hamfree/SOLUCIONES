#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pylint: disable=E1601
"""
 17/02/2018
   Profesores: Álvaro Sánchez de Cruz / ???
   - Se hace un repaso de lo que se impartió el día anterior.
   - Subprogramas o funciones:
       - Viene de la programación estructurada.
       - Sintaxis:
           def nombreFuncion([parametro1,][parametro2,]...)
               (codigo de la funcion)
               [return valor]

 
   Los valores se pasan siempre por valor a las funciones.
   Ahora vamos a ver un ejemplo:

    def saludo()
        print "Hola Mundo"

    - Se explican los ejercicios propuestos del día 1.

    - Ficheros
       var = open('ruta al fichero','a'|'r'|'w')

    - JSON
        Es un formato de datos originario de JavaScript, que hablando en terminologia de python es una
         lista de diccionarios, de la siguiente forma:

        [
            {},{},...
        ]

        En python los JSON se pueden pasar a un diccionario muy facilmente.

"""
# modo 'r' read, que lee el fichero si existe y si no dara un error
def leerFichero():
    f = open('clase.py','r')
    print "Contenido de 'clase.py'"
    print "-----------------------"
    for l in f:
        print l

# modo 'a' append, que añade al fichero si existe y si no lo crea
def sobreescribirFichero():
    f = open('prueba.txt','a')
    for i in [1,3,5,7,9,21,12,32,23]:
        f.write('Hola' + str(i) + '\n')
    f.close()



# modo 'w' write, que escribe en el fichero si existe, sobreescribiendo lo que tuviera, y si no lo crea.
def leerEscribirFichero():
    fr = open('clase.py','r')
    fw = open('copia de clase.py','w')
    for l in fr:
        fw.write(l)
    fr.close()
    fw.close()

leerFichero()
sobreescribirFichero()
leerEscribirFichero()




