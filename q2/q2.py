#function to check number of occurence of number
def myFunc(array,num):
    return sum(x.count(num) for x in array)

#declare values array
value_list = [[1,2,3], [5,6],[5,7]]
print(myFunc(value_list,5))