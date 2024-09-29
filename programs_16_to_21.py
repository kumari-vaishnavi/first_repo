#give a list and find the average of it:
def a(n):
    sum_numbers=sum(n)
    len_numbers=len(n)
    average=sum_numbers/len_numbers
    return average
print(a([4,5,1,2]))

#give a list and find the number of even numbers:
def even_numbers(data):
    i=0
    for n in data:
        if n%2==0:
          i=i+1
    return i
print(even_numbers([9,3,4,2,6,7,8,10]))

#give a list find all the even numbers and sum of it and return result:
def even(data):
    count = 0
    for i in data:
        if i%2 == 0:
            count = count + i
    return count
print(even([1,2,3,4,5,6]))

#give a list of all odd numbers and sum it and return the result:
def odd(data):
    count = 0
    for i in data:
        if i%2 != 0:
            count  = count + i
    return count
print(odd([1,2,3,4,5,6]))
