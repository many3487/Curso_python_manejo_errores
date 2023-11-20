
'''def sum_with_range(a,b):
    sum =0
    for x in range(a,b):
        sum +=x 
    print (sum)
    
sum_with_range(50,200)'''

#con return
def sum_with_range(a,b):
    sum =0
    for x in range(a,b):
        sum +=x 
    return sum
    
result = sum_with_range(1,3)
print (result)

result_2 = sum_with_range(result, result +50)
print (result_2)
