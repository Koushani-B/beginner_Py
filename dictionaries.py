#creating an empty dictionary
empty_dict = {}
#dictionary w data val
dct = {'key1': 'val1', 'key2':'val2', 'key3':'val3', 'key4':'val4'}
print(dct)
#val within a dict couuld be any data types - boolean, list, tuple, set or a dictionary
#finding the length of a dictionary using len() syntax
print(len(dct))
#accessing dictionary items by referring to its key name
print(dct['key1']) #would prefer this method
print(dct['key2'])
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

print(project)
print(project['first_item'])
print(len(project))
#.get() returns none if the key val doesnot exist
print(project.get('first_item'))
print(project.get('city'))
#adding items to the dictionary
dct['key5'] = 'val5'
print(dct)
project['PhD_year'] = '3rd'
print(project)
project['key_words'].append('multiunit')
print(project)
#modifying items in a dictionary
project['first_item'] = 'The ACC'
print(project)
#checking keys in a dictionary using syntax in
print('key5' in dct)
print('key6' in dct)
#removing key and val pairs from a dict
#pop(key) - removes the item with specified key name
#popitem() - removes the last item
#del - removes an item with a specified key name
dct.pop('key5')
print(dct)
dct.popitem()
print(dct)
del dct['key2']
print(dct)
#adding the itens back
dct['key4'] = 'val4'
print(dct)
#to add say key2 we can modify the key3 and then add another key5 later on
dct.pop('key3')
print(dct)
dct.pop('key4')
print(dct)
dct['key2'] = 'val2'
dct['key3'] = 'val3'
dct['key4'] = 'val4'
print(dct)
#changing dictionary to a list  item using syntax items()
print(dct.items())
#changing the list back to dictionary
dct = dict(dct)
print(dct)
#we can clear a dictionary using .clear()
#we can delete a dictionary using del
#copying a dictionary using copy()
dct_copy = dct.copy()
print(dct_copy)
#getting dictionary keys as a list
keys = dct_copy.keys()
print(keys)
#getting dictionary values as a list
val = dct_copy.values()
print(val)
dct_copy.clear()
print(dct_copy)
del dct_copy
