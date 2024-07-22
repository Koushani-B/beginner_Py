#creating an empty list
List_1 = []
print(List_1)
#declaring a list with 5 variables 
List_2 = ['item1', 'item2', 'item3', 'item4', 'item5']
print(List_2)
#finding the length of the list2
print(len(List_2))
#accessing specific items in the list - first, mid and tge last item from the list
first_item = List_2[0]
second_item = List_2[2]
third_item = List_2[4]
print(first_item, second_item, third_item)
it_companies = ['facebook', 'google', 'microsoft', 'apple', 'IBM']
print(it_companies)
print(len(it_companies))
first_item, second_item, third_item, *rest = it_companies
print(it_companies)
it_companies.insert(3, 'Oracle')
print(it_companies)
first_company = it_companies[0]
print(first_item)
mid_company = it_companies[2]
print(mid_company)
last_company = it_companies[-1]
print(last_company)
print(it_companies.sort())
print(it_companies.sort(reverse=True))
test = [1, 2, 3, 4]
test.sort()
print(test)
print(test.sort(reverse=True))
del it_companies[0:3]
print(it_companies)
it_companies.insert(0, 'facebook')
print(it_companies)
it_companies.insert(1, 'google')
print(it_companies)
it_companies.insert(2, 'microsoft')
print(it_companies)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)
#joining two lists
full_stack = joined_list.copy()
print(full_stack)
#inserting an item in a joined list
full_stack.insert(5, 'Python')
print(full_stack)
full_stack.insert(6, 'SQL')
print(full_stack)
#printing a new list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
#sorting the list in ascending and descending order
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)
ages.insert(0, 19)
print(ages)
ages.insert(-1, 26)
print(ages)
average = sum(ages) / len(ages)
print(average)
max_l = max(ages)
print(max_l)
min_l = min(ages)
print(min_l)
range_l = max_l - min_l
print(range_l)
#using syntax abs() for getting absolute val
min_avg_diff_abs = abs(min_l - average)
max_avg_diff_abs = abs(max_l - average)
#comparing the two val
comparison = min_avg_diff_abs is max_avg_diff_abs
print(comparison)
print(f'minimum val: {min_l}')
print(f'maximun_val: {max_l}')
print(f'average_vak: {average}')
print(f'absolute_difference (min - average): {min_avg_diff_abs:.2f}')
print(f'absolute_difference (max - average): {max_avg_diff_abs:.2f}')
print(f'The absolute difference (min - average) is {comparison}')
