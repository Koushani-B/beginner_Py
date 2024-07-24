#input user name 
Age = int(input('Enter your Age')),
years = 18 - Age
if Age >= 18:
    print('You are old enough to drive!')
else:
    print(f"You need {years} years to learn to drive")
#comparing ages using nested conditions
my_age = 26
#get user input
your_age = int(input('Enter your age:'))
#calcuulate the age difference
age_difference = your_age - my_age
age_difference_2 = my_age - your_age
if your_age > my_age:
    if age_difference == 1:
        print('You are one year older than me!')
    else:
        print(f"youu are {age_difference} years older than me")
elif your_age < my_age:
    if age_difference_2 == 1:
        print('I am one year older than you')
    else:
        print(f"I am {age_difference_2} older than you")
else:
    print('We are of same age!')
#user input for two numbers
num_1 = int(input('Enter the first number:'))
num_2 = int(input('Enter the second number:'))
if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_1 < num_2:
    print(f"{num_1} is less than {num_2}")
else:
    print(f"{num_1} is equal to {num_2}")

#assigning grades to students
score = int(input('Enter the score out of 100:'))
if score >= 80:
    print('Grade A')
    if score == 100:
        print('Grade A')
elif score >= 70:
    print('Grade B')
    if score == 79:
        print('Grade B')
elif score >= 60:
    print('Grade C')
    if score == 69:
        print('Grade C')
elif score >= 59:
    print('Grade D')
    if score == 50:
        print('Grade D')
else:
    print('Grade F')
#seasons 
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
month = input('Enter month here:')
if month in autumn:
    print('Autumn')
elif month in winter:
    print('Winter')
elif month in spring:
    print('Spring')
else:
    print('Summer')
#adding things to a list using conditionals
fruits = ['banana', 'orange', 'mango', 'lemon']
to_add = input('what is your favorite fruit? ')
if to_add in fruits:
    print('That fruit already exists')
else:
    fruits.append(to_add)
    print('Modified list of fruits:', fruits)
