import os

print( u"¡Hola mundo!")
os.system('pause')
os.system('cls')
lista = ['cero','uno','dos','tres','cuatro','cinco']
# Bucle simple que recorre la lista a
print('Bucle que muestra los elementos de la lista y la longitud en caracteres de cada elemento')
for a in lista:
    print(a, len(a))
os.system('pause')
os.system('cls')
# Bucle que itera sobre un rango de números, de 0 a 10
print('Bucle que muestra los números del 0 al 10')
for b in range(10):
    print(b,sep=' ',end='')
os.system('pause')
os.system('cls')
# Bucle que itera sobre un rango de números, de 10 a 20, con un salto de 2
print('Bucle que muestra los números del 10 al 20, con saltos de 2')
for c in range(10,20,2):
    print (c,sep=' ',end='')
os.system('pause')
os.system('cls')
# Bucle que itera la lista usando sus índices
print('Bucle que muestra la lista utilizando los indices')
for i in range(len(lista)):
    print(i,lista[i],sep=':',end='\n')
    