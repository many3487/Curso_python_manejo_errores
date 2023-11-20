import random
countries = ['col','mex','bol','pe','bol']

population_2 ={country: random.randint(1,100) for country in countries}
print(population_2)

resultado = { country : population for (country, population) in population_2.items() if population > 20}
print(resultado)

texto = "hola, soy many"
unique = {caracter: caracter.upper() for caracter in texto if caracter in 'aeiou'}
print(unique)

