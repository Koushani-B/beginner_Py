#string could be made using a single or a double quote
#multiline strig is made using a triple double  or single quotes
sentence = "This is day 4th of learning python"
print(sentence)
sentence_1 = 'This is day 4th of learning python'
print(sentence_1)
multiline_string = """Text is a string data type.
Any data type written as a text is a string.
Any data under a single, double or triple quote are strings."""
print(multiline_string)
#string concatenation - merging or connecting strings
first_part = 'Hippocampus'
second_part = 'Cerebellum'
space = ' '
full_part = first_part + space + second_part
print(full_part)
print(len(first_part))
print(len(second_part))
print(len(first_part) >= len(second_part))
#escape sequences in strings
#\n - new line
#\t - tab means
# \\ back slash
#\' - single quote
#\" double quote
print('This is the python challenge. \nAm I ?')
print('Days\tTopics\tExercises') #adding tab space or 4 spaces
print('Day1\t5\t5')
print('Day2\t6\t20')
print('Day3\t5\t23')
print('This is a backslash symbol (\\)')
print('In every programming language it starts with \"Hello, world!\"') #double quotes inside
#string formatting
# % - used to foemat a set of variables enclosed within a tuple 
# %s - string (string rep - like numbers)
# %d - integers
# %f - floating point numbers
# %.number of digitsf" - floating point numbers w fixed precisions
#writing w strings only
ch_1 = 'Cerebellum'
ch_2 = 'Hippocampus'
ch_3 = 'Associative learning'
formatted_string  = 'The role of %s and %s in %s' %(ch_1, ch_2, ch_3)
print(formatted_string)
#strings and numbers
radius = 10
pi = float(3.14)
area = pi * radius ** 2
f_string = 'The area of the circle with a radius of %d is %.2f' %(radius, area)
print(f_string)
#new version of formattingg - {} and str.format
new_formatted_string = 'The role of {} and {} in {}'.format(ch_1, ch_2, ch_3)
print(new_formatted_string)
#numerical operations using string formatting
a = 2
b = 10
print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(b, a, b-a))
print('{} * {} = {}'.format(a, b, a*b))
print('{} **{} = {}'.format(a, b, b**a))
#area of the circle with pre determined val
new_f_string = 'The area of the circle with a radius of {} is {:.2f}.'.format(radius, area)
print(new_f_string)
#interpolation  fstrings - strings starting with f and can inject the data in their corresponding position
print(f'{a} + {b} = {a+b}')
print(f'{b} - {a} = {b-a}')
print(f'{a} * {b} = {a*b}')
print(f'{a} ** {b} = {a**b:.2f}') #:.2f - shows that we will be going uptil 2 decimal places
#unpacking characters 
language = 'python'
c, d, e, f, g, h = language
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
#accessing characters in strings by index
first_letter = language[0]
print(first_letter)
last_letter = language[-1]
print(last_letter)
#can also index last letter as
#last_index = len(language)-1
#last letter = language[last_index]
#######################################################
#slicing python strings into substrings using index
first_three = language[0:3]
print(first_three)
last_three = language[3:]
print(last_three)
#skipping characters while slicing
pto = language[0:6:2]
print(pto)
#string methods 
#.capitalize()
challenge = 'thirty days of python'
print(challenge.capitalize())
#.count() - returns occurences of substring in a string
print(challenge.count('y'))
print(challenge.count('pyth'))
#.endswith() - returns if  the string ends w a specific ending
print(challenge.endswith('n'))
#.expandtabs()- replaxes tab character with spaces of choice of size
challenge_2 = 'thirty\tdays\tof\tpython'
print(challenge_2.expandtabs(10))
# .find() r eturns the index of the first occurebce of a substring if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))
# .index() - returns the lowest index of a substring 
# .rindex() - returns the highest level of a substring
sub_string = 'da'
print(challenge.index(sub_string))
print(challenge.index(sub_string, 9)) # will give val error since stated substring is not at 9th positio
print(challenge.rindex(sub_string))
# .isalnum - check alphanumeric character - if all characters are alphabetic 
#would return false whenn there's a space
print(challenge.isalnum())
#.isalpha()
print(challenge.isalpha())
challenge_3 = 'thisisathirtydayofpythonchallenge'
print(challenge_3.isalpha())
# isdecimal() - checks if all characters in a string are decimal
print(challenge.isdecimal())
# .isnumeric() - checks if the chars are in a string are numeric, just like .isdigit() but accepts more charaters
num = '10'
print(num.isnumeric())
print(num.isdigit())
# .isidentifier() - checks for valid identifier - checks if a string  has a valid variable name
# .islower() - checks if all alphabets are in lowercase
# .isupper() - checks if all the alphabets are in uppercase
# .join() - returns the concatenated string ???
# strip()- removes all given character starting from the beginning and end of the strog
print(challenge.strip('thon'))
test = ['a', 'b', 'c', 'd']
result = '#'.join(test) #returns a concatenated string
print(result)
# .replace() - replaces a substring with a given string
print(challenge.replace('python', 'coding'))
