#set is a collection of unordered an unindexed distinct elements
#creating a set using syntax set()
#empty set
empty_set = set()
print(empty_set)
#creating a filled set using {} operators
set_1 = {'item1', 'item2', 'item3', 'item4', 'item5'} #will return unordered items
print(set_1)
#getting the length of a set
print(len(set_1))
#now to access items within a set we will be using loops
#to check if an item is present in the set we will use 'in' membership operator
print("Does set set_1 contain item 3?", 'item3' in set_1)
#adding items to a set using add()
set_1.add('item6')
print(set_1)
#we can actually add multiple items using update(); update takes a list as an argument
set_1.update(['item7', 'item8', 'item9'])
print(set_1)
#removing an item from a set could be done using remove() or discard(); remove will raise an error if the item is not found while discard wont raise any error
set_1.remove('item10')
set_1.discard('item10')
set_1.remove('item9')
print(set_1)
#pop() removes a random item from the set
#to clear the whole set we use .clear()
#to delete the whole set we use del operator
del set_1
print(set_1)
#converting a list to a set we will use the set() opeartor
list_1 = ['item10', 'item11', 'item12', 'item13']
set_new = set(list_1)
print(set_new)
#we will be joinining two sets using .union()
set_2 = set_1.union(set_new)
print(set_2)
#inserting one set into another one using .update()
set_3 = set_2.update(set_1)
print(set_3)
#finding intersection items usingg .intersection()
set_2.intersection(set_new)
#checking subset or a superset using .subset() or .superset()
set_2.issubset(set_new)
set_new.issuperset(set_2)
set_2.issuperset(set_new)
#checking the diff bw two sets using .difference()
set_new.difference(set_2)
set_2.difference(set_new)
#finding symmetric differences bw two sets uusng .symmetric_differences(); (A\B) ∪ (B\A)
set_2.symmetric_difference(set_new)
#joining two sets
#but first gotta check if our sets are joint or disjoiint using .disjoint()
set_new.isdisjoint(set_1)#returns true when there's no common item
#returns false when there's a common item

###################################################
