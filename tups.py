#tuple is a collecyion of diff data types which is ordered and UNCHANGEABLE
# tuples are written in ()
# we cannot change the val of a tuple unlike a string or a list
#creating an empty tuple
empty_tuple = ()
#whereas when we create a list we are  usig [] t create an empty list
#we can also use a tuple constructor to create a tuple
empty_tuple1 = tuple() 
print(empty_tuple)
print(empty_tuple1)
#tuple w initial val
tuple_1 = ('item1', 'item2', 'item3')
#getting the length of a tuple
len(tuple_1)
#accessing tuple items with syntax []
first_item = tuple_1[0]
second_item = tuple_1[1]
print(first_item)
print(second_item)
#negattive indexing to index a tuple
first_item_neg = tuple_1[-3]
last_item_neg = tuple_1[-1]
print(first_item_neg)
print(last_item_neg)
#gotta slice some tups now - what if we want to recall just a couple of items from the tup
all_items = tuple_1[0:3]
all_items_n = tuple_1[0:]
print(all_items_n)
print(all_items)
#recalling certain items using negative index
all_items_neg = tuple_1[-3:]
all_items_neg_n = tuple_1[-3:-1] #doesnot include the last item
print(all_items_neg)
print(all_items_neg_n)
#gotta change tthe tups tto list by using syntax list()
list_1 = list(tuple_1)
print(list_1)
list_1.insert(3, 'item 4')
print(list_1)
#now changing the list back to a tup using syntax tuple()
list_1 = tuple(list_1)
print(list_1)
#gotta check a specific item in a tup using syntax in ''
'item2' in tuple_1
# if we wanna add an item in a tup, we gotta change the tup in a list and insert our select item and then change it into a tup again
#OR we can change the tup in a list and make a copy of it and work on the copy
#joining two tups with +  operator
tuple_2 = ('item5', 'item6', 'item7', 'item8')
new_tuple = tuple_1 + tuple_2
print(new_tuple)
#deleting a tup using a del function but we cannot singularly delette a particular item from a tup
#so if we wanna delete something, we gotta change iit into list and delete it and change it back to a tup
del(tuple_2)
print(tuple_2) # would return name error
