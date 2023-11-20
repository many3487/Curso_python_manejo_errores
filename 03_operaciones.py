set_a ={'col','mex','bol'}
set_b = {'pe','bol'}

set_c = set_a.union(set_b)
print (set_c)

print (set_a | set_b)

#interseccion
set_c = set_a.intersection(set_b)
print (set_c)
print (set_a & set_b)


#diferencia
set_c = set_a.difference(set_b)
print(set_c)

print (set_a - set_b)

#diferencia simetrica hacer una union din los elementos que coinciden en comun

set_c = set_a.symmetric_difference(set_b)
print(set_c)
print (set_a ^ set_b)








