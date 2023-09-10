diccionario1 = {'str':'esto es un string' , 'char':'C' , 'list':['elemento 1','elemento 2','elemento 3']}

print('str ->', diccionario1['str'])
print('char ->', diccionario1['char'])
print('list ->', diccionario1['list'])

print("\nMostramos las claves del diccionario 'diccionario1'")
print(diccionario1.keys())
print("\nMostramos los valores del diccionario 'diccionario1'")
print(diccionario1.values())

print('\nAhora actualizamos el diccionario\n')
diccionario1['str'] = 'esto ya es otro string'
diccionario1['int'] = 7

print('str ->', diccionario1['str'])
print('char ->', diccionario1['char'])
print('list ->', diccionario1['list'])
print('int ->', diccionario1['int'])

print("\nMostramos las claves del diccionario 'diccionario1'")
print(diccionario1.keys())
print("\nMostramos los valores del diccionario 'diccionario1'")
print(diccionario1.values())