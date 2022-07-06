diccionario1 = {'str':'esto es un string' , 'char':'C' , 'list':['elemento 1','elemento 2','elemento 3']}

print diccionario1['str']
print diccionario1['char']
print diccionario1['list']

print diccionario1.keys()
print diccionario1.values()

print 'ahora actualizamos el diccionario'
diccionario1['str'] = 'esto ya es otro string'
diccionario1['int'] = 7

print diccionario1['str']
print diccionario1['char']
print diccionario1['list']
print diccionario1['int']

print diccionario1.keys()
print diccionario1.values()