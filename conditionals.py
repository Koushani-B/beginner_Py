#conditional execution - block would be executed if a certain expression is true
#repetitive execution - block would be executed repetitively until a certain expression is deemed to be true
#if condition
#if condition:
    #this part of the code runs for truthy conditions
a = 3
if a>0:
    print('A is a positive number')
#if and else
# if - runs for truth conditions
# else - runs for false conditions
b = -2
if b > 0:
    print('B is a positive number') 
else:
    print('B is a negative number') 

#if elif else conditions
# when we have multiple conditions we use elifs
c = 0
if c>0:
    print('C is a positive number')
elif c<0:
    print('C is a negative number') 
else:
    print('C is zero') 
#writing the conditions in short hand
#syntax - code if condition else code
d = 3
print('D ois positive') if d > 0 else print('D is negative')
#nested conditions
#syntax -
#if condition:
    #code
    #if condition:
     #code
e = 0
if e > 0:
    if e % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive integer')
elif e == 0:
    print('E is zero')
else:
    print('A is a negative number')
#using if conditions and logical operators
# and is a logical operator
if e>0 and e%2 == 0:
    print('E is an even and positive integer')
elif e>0 and e%2 != 0:
    print('A is a positive integer')
elif e == 0:
    print('E is zero')
else:
    print('E is negative')

#if and or logical operators
#syntax -
#if condition or condition:

user = 'Koushani'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')
