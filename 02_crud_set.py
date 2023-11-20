set_countries = {'col','mex','bol'}

size = len(set_countries)
print (size)

print('col' in set_countries)
print('per' in set_countries)


##addicionar
set_countries.add('per')
print(set_countries)


#update

set_countries.update({'arg','ecu','per'})
print(set_countries)

#delete
#remove
set_countries.remove('per')
print(set_countries)
#si el elemento no existe y uso remove, el programa se puede estallar para evitar esto se usa
set_countries.discard('per')
print(set_countries)
#para borrar todo el conjunto se usa clear
set_countries.clear()
print(set_countries)