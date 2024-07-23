#creating an empty dictionary
dog = {}
#filling up the dictionary
dog = {
    'Name':'Bruno',
    'Breed':'Husky',
    'legs':4,
    'age':12
}
print(dog)
#creating a student dictionary
student = {
    'first_name':'Koushani',
    'lastname':'Biswas',
    'gender':'female',
    'age': 26,
    'skills': ['ephys', 'CPP', 'Python'],
    'country':'India',
    'city':'Kolkata',
    'Address':{
        'street':'anushakti',
        'pin': 00000
    }
}
print(student)
#getting the length of the dictionary
print(len(student))
#getting the value of skills 
print(student.get('skills'))
#modiifying the skills values  by adding more skills
student['skills'].append('microscopy')
print(student)
#getting dictionary keys as a listt
key = student.keys()
print(key)
#getting dictionary vals as a list
val = student.values()
print(val)
#changing dct to a list of tups
print(student.items())
