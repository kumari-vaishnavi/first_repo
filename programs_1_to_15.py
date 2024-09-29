

#write a program to add 3 numbers:
def adding_3_numbers(a,b,c):
 add=a+b+c
 return add
print(adding_3_numbers(4,6,44))

#write a program to subtract 3 numbers:
def subtracting_3_numbers(d,e,f):
 subtract=d-e-f
 return subtract
print(subtracting_3_numbers(20,6,3))

#write a program to multiply 3 numbers:
def multiplication_3_numbers(a,b,c):
 multiply=a*b*c
 return multiply
print(multiplication_3_numbers(8,9,2))

#write a program to divide_3_numbers:
def dividing_3_numbers(f,g,h):
 divide=f/g/h
 return divide
print(dividing_3_numbers(40,4,3,))

#write a program to sqaure a number:
def square_number(v):
 square=v*v
 return square
print(square_number(17))

#write a program to cube a number:
def cubing_number(v):
 cube=v*v*v
 return cube
print(cubing_number(2))

#write a program with a number(n) and power (x), find n to the power x:
def power_number(n,x):
 power=pow(n,x)
 return power
print(power_number(5,2))

#find the length of string without using len():
def length_of_string(data):
 result=0
 for i in data:
  result=result+1
 return result
data="opinion"
print(length_of_string(data))

#give a list of integers and add all the numbers and return the total without using sum():
def list_of_intergers(data):
    i = 0
    for num in data:
        i = i+ num
    return i
print(list_of_intergers([1,2,3,-4,5]))

#give a list and find the number of even numbers:
def even_numbers(data):
    i=0
    for n in data:
        if n%2==0:
          i=i+n
    return i
print(even_numbers([9,3,4,2,6,7,8,10]))

#give a list and find number of odd numbers:
def a(num):
    i=0
    for n in num:
        if n%2!=0:
         i=i+1
    return i
print(a([4,5,6,7,8,9,0]))

