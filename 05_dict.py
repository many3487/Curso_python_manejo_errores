###################### diccionarios #####################
print('*'*50)
names = ['nico', 'zule', "santi"]
edades = [12,56,98]
new_dict = {names[i]:edades[i] for i in range(len(names))}

##los deben tener clave valor
dict= {}
for i in range(1,11):
    dict[i] = [i*2]
print (dict)

dict_2 ={i: i*2 for i in range(1 , 5)}
print (dict_2)


########
import random
countries = ['col','mex','bol','pe','bol']
population ={}
# Utilizar un bucle 'for' para iterar sobre cada país en la lista 'countries'
for country in countries:
    # Asignar un valor aleatorio entre 0 y 100 al país actual en el diccionario 'population'
    population[country] = random.randint(0, 100)
print(population)

population_2 ={country: random.randint(1,100) for country in countries}
print(population_2)

names = ['nico', 'zule', "santi"]
edades = [12,56,98]

print(zip(names,edades))
#aparece <zip object at 0x000001F783A8FF40> si aparece esto es porque se debe convertir en una lista y para esto se hace de la siguiente manera:
print(list(zip(names,edades)))
#da una lsita con tuplas ahora acrear el diccionario
new_dict = {name: edades for (name, edades) in zip(names,edades)}
print(new_dict)

