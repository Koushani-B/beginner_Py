#while and for loop
#while loop executes a block repeatedly until a given condition is satisfied 
#if the condition becomes false - lines after the loop  would be continued to be executed
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
#break syntax is used when we want to get out of the loop or stop the loop
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
#skipping 3 using syntax continue
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
else:
    print(count) #will count till 5
#for loop with a list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)
#for loop with string
language = 'python'
for letter in language:
    print(letter)
#loop wih tuple
nums = (0,1,2,3,4,5) 
for num in nums:
    print(num)
#for loop with dictionary
project = {
    'first_item':'ACC',
    'second_item':'HPC',
    'third_item':'Cerebellum',
    'in_progress':True,
    'key_words':['ephys', 'tebc', 'matlab'],
    'conference':{
        'name_1': 'pav',
        'name_2': 'sfn'
    }
}
for key in project:
    print(key)

for key, value in project.items():
    print(key, value)
#loop in a set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
#break and continue
digits = (0, 1, 2, 3, 4, 5)
for digit in digits:
    print(digit)
    if digit == 3:
        continue
    print('The next digit should be ', digit + 1) if digit != 5 else print("loop has ended")
print('outside the loop')
#range function
list_1 = list(range(11))
print(list_1)
set_1  = set(range(1, 11))
print(set_1)
list_2 = list(range(0,12,2)) #the third argument mentions the step
print(list_2)
set_2 = set(range(0, 12, 2))
print(set_2)
#nested for loops
project = {
    'first_item':'ACC',
    'second_item':'HPC',
    'third_item':'Cerebellum',
    'in_progress':True,
    'key_words':['ephys', 'tebc', 'matlab'],
    'conference':{
        'name_1': 'pav',
        'name_2': 'sfn'
    }
}
for key in project:
    if key == 'key_words':
        for keyword in ['key_words']:
            print(keyword)
#for else 
for digits in range(11):
    print(digits)
else:
    print('The loop stops at', digits)
#pass - placeholder for statements after colon
for number in range(10):
    pass
