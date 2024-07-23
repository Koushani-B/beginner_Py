# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#finding length of it_companies
print(len(it_companies))
#adding twitter to it com
it_companies.add('twitter')
print(it_companies)
#adding multiple companies to a set
it_companies.update(['open ai', 'neuralink'])
print(it_companies)
#removing an item from a set
it_companies = list(it_companies)
print(it_companies)
it_companies.remove('neuralink')
print(it_companies)
it_companies = set(it_companies)
print(it_companies)
it_companies.remove('Amazon')
print(it_companies)
#joining two sets
newset = A.union(B)
print(newset)
#finding intersection
A.intersection(B)
#is A a subset of B
A.issubset(B)
#are they disjoint sets
A.isdisjoint(B)
newset_1 = B.update(A)
print(newset_1)
#finding symmetric differences
A.symmetric_difference(B)
B.symmetric_difference(A)
del(A)
del(B)
set_age = set(age)
print(set_age)
print(len(set_age))
print(age)
print(len(age))
sentence = ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire',  'and',  'teach', 'people']
print(sentence)
new_sentence = 'I am a teacher and I love to inspire and teach'
print(new_sentence.split(','))
substring = 'I'
substring_1 = 'teacher'
substring_2 = 'and'
print(new_sentence.find(substring))
print(new_sentence.find(substring_1))
print(new_sentence.find(substring_2))
