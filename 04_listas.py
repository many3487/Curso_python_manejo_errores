days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
newlist = []

for i in days:
  if "a" in i:
    newlist.append(i)

print(newlist) #["martes", "sabado"]


numbers =[]
for element in range(1, 11):
  numbers.append(element)

print(numbers)
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

numbers =[]
for element in range(1, 11):
  numbers.append(element *2)
print(numbers)

numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)
###########
print('*'*50)
numbers =[]
for i in range(1, 11):
  if i % 2 ==0:
    numbers.append(i *2)
print(numbers)

number_v2 = [element*2 for element in range(1, 11) if element % 2 ==0] 
print(number_v2)


