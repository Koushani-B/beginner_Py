#concatenate
test = ['Thirty', 'days', 'of', 'python']
print(' '.join(test))
#concatenate 2
test_2 = ['Coding', 'For', 'All']
print(' '.join(test_2))
Company = ('Coding for all')
print(Company)
#printing the length
print('The length of the variable is:', len(Company))
#changing to upper case
print(Company.upper())
#changing to lower case
print(Company.lower())
#changing to cap
print(Company.capitalize())
print(Company.title()) #caps the first letter of each word in the string'
print(Company.swapcase()) #swaps the lower to upper cases and vice versa in the string
print(Company.strip('Coding')) #slicing the first word off the string
sub_string1 = 'Coding'
print((Company.find('Coding')))
print(Company.index(sub_string1)) #finding and indexing a value within a defined string
print(Company.replace('Coding', 'Python')) #replacing a val within a string with another val
Company_2 = ('Python for everyone')
print(Company_2.replace('everyone', 'all'))
#splitting the string
print(Company.split( ))
test_2 = ('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon')
print(test_2.split(','))
#accessing letters in a string using indexing
index_0 = Company[0]
print(index_0)
index_10 = Company[11]
print(index_10)
acr = Company[:6:9]  #get back to solve it
print(acr)
print(Company.index('C'))
print(Company.index('f'))
print(Company.rindex('l'))
test_3 = 'You cannot end a sentence with because because because is a conjuction'
sub_string_new = 'because'
print(test_3.find(sub_string_new))
print(test_3.rindex(sub_string_new))
sliced = test_3[31:54]
print(sliced)

