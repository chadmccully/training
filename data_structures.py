#data structures
# list
# marks = [45, 54, 80]
# sum(marks)
# sum(marks)/len(marks)
# marks.append(43)
# same math works
# type(marks) is class 'list'
# structure is squared brackets, values, commas between.
# marks = [ a, b, c, d, e]
#sum(marks)
#max(marks)
#min(marks)
#len(marks)
#marks.append(f)
#marks prints the list
#marks.insert(2, 60) will add the value in 0, 1, *2 element
# f in marks will respond with true or false
# marks.index(f) will return the index of the value in the array
# for mark in marks:
#     print(mark)
# this will loop through the values and print them

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def get_number_of_marks(self):
#         return len(self.marks)
#
#     def get_total_sum_of_marks(self):
#         return sum(self.marks)
#
#     def determine_maximum_mark(self):
#         return max(self.marks)
#
#     def determine_minimum_mark(self):
#         return min(self.marks)
#
#     def determine_average(self):
#         return self.get_total_sum_of_marks()/ self.get_number_of_marks()
#
#     def add_new_mark(self, new_mark):
#         self.marks.append(new_mark)
#
#     def remove_mark_at_index(self, index):
#         del self.marks[index]

 #   def remove_mark_at_index(index_of_mark):

# student = Student("Adam", [25, 75, 98, 35, 63, 69])
# number = student.get_number_of_marks()
# print(f"Student: {student.name} [marks - {student.marks}]")
# print(f"Student: {student.name} [number of marks-{number}]")
# sum_val = student.get_total_sum_of_marks()
# print(f"Student: {student.name} [sum of marks-{sum_val}]")
# max_val = student.determine_maximum_mark()
# print(f"Student: {student.name} [max mark-{max_val}]")
# min_val = student.determine_minimum_mark()
# print(f"Student: {student.name} [min mark-{min_val}]")
# avg_val = student.determine_average()
# print(f"Student: {student.name} [avg of marks-{avg_val}]")
# student.add_new_mark(35)
# number = student.get_number_of_marks()
# print(f"Student: {student.name} [number of marks-{number}]")
# print(f"Student: {student.name} [marks - {student.marks}]")
# print(f"Student: {student.name} [sum of marks-{sum_val}]")
# student.remove_mark_at_index(2)
# number = student.get_number_of_marks()
# print(f"Student: {student.name} [number of marks-{number}]")
# print(f"Student: {student.name} [sum of marks-{sum_val}]")
# print(f"Student: {student.name} [marks - {student.marks}]")

#animals = ['Cat', 'Dog', 'Elephant']
# len(animals)
# sum(animals) <- error
# animals.append('Fish')
# animals.remove('Dog')
# animals <- displays list of the elements
# animals[2] displays the 3rd element
# animals.remove('Dog') isn't same as del animals[2] .... remove by value use remove.  remove by index use del
# animals.extend('Fish') will take the word Fish and add each letter as separate elements.  Append adds the element
# animals.extend(['Giraffe','Horse','Frog']) will add the animals individually
# animals = animals + ['Jackal', 'Kangaroo'] will extend to the list
# animals += ['Lion','Monkey'] will do it, too
# animals.append(10) will add the value 10... no type restrictions.  Values can be of any type

# numbers = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
# len(numbers will show 10 elements
# number[2] will present 'Two'
# numbers[2:6] will bring in from element 2 to 5, excluding 6
# ['Two','Three','Four','Five']
# numbers[:6] will bring in up to element 5 assuming 0 as starting element
# numbers[3:] will do the same... from index to end of list
# Can slice/dice the list any way you like
# numbers[1:8:2] will start at 1 and end at 7, skipping every other one, incrementing by the third value
# number[::3] will get every third element
# number[::-1] will get you the reverse of the list
# number[::-3] will get reverse from top to bottom of list
# can use slicing to delete elements from the list
# del numbers[5:7] will remove elements 5 and 6
# can replace values as well
# numbers[3:5] = [3, 4, 5] will replace the three, four, and five with their numeric values

# code to sort, reverse, etc. with lists
# numbers.reverse <= will reverse the order of the elements - it changes the order of elements
# reversed(numbers) gives you the ability to access the list in reverse, but does not change the actual order
# for number in reversed(numbers):
#     print(number)
# will show the items in reversed order
# numbers.sort()
# Since these are strings, it will sort in alphabetical order, and it modifies the array
# sorted(numbers) will give you that same sort but not modify the array
# for number in sorted(numbers):
#     print(number)
# for number in sorted(numbers, key="len") will sort by length
#     print(number)
# for number in sorted(numbers, key="len", reversed=True):
#     print(number)
# key can be a function which can be supported as well
# numbers.sort function can use these as well, such as (key=len) or (key=len, reverse=True)

#features of lists: stacks and queues
# a stack is usually LIFO (1,2,3,4) comes out as 4,3,2,1 when retrieved
#numbers = []
#numbers.append(1)
#numbers.append(2)
#numbers.append(3)
#numbers.append(4)
#numbers.pop() will retrieve the last element and will delete it as well

#queue use for a list
#numbers = []
#numbers.append(1)
#numbers.append(2)
#numbers.append(3)
#numbers.append(4)
#numbers.pop(0) will pull out the first element, retrieve it, and delete it as well
# can do this differently by using a dequeue, but until then it works.

#list comprehension
#numbers = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
#numbers_length_four=[]
#for number in numbers:
#    if len(number)== 4:
#        numbers_length_four.append(number)
#list comprehension allows this to go more rapidly
# numbers_length_four = [number for number in numbers]
#
# numbers_length_four = [len(number) for number in numbers]
# creates [4,3,3,5,4,4,3,5,5,4]
# or number.upper() which will create text in all caps
#
# numbers_length_four = [number for number in numbers if len(number)==4]
# this will create list of only 0 4 5 and 9, but puts it in a single line.  It's called list comprehension

# values = [3, 6, 9, 1, 4, 15, 6, 3]
#
# #create list with even numbers only
# even_values = []
# even_values = [value for value in values if value%2 == 0]
# print(even_values)
#Lists can contain duplicates
# more based on the index
# in lists the position is given the utmost importance

#set doesn't contain duplicates
# numbers_set = set(numbers)
# numbers_set will then have {1,2,3}
# numbers_set.add(3) if already there would only be there 1 time. If new entry (non-duplicate) it will be not added
#
# Sets don't use indexes... it is referenced by value only.
# 1 in number_set will be True or False
#
# min(number_set) is allowed, as is max or sum or len if they are on all the values together
#
# numbers_1_to_5_set = set(range(1,6))
# numbers_4_to_10_Set = set(range(4,11))
# numbers_1_to_5_set + numbers_4_to_10_set is not a valid option
#
# Can do numbers_1_to_5_set | numbers_4_to_10_set though, which will create a union of the two (distinct values)
# for intersection of the two sets numbers_1_to_5_set & numbers_4_to_10_set
#
# Can do numbers_1_to_5_set - numbers_4_to_10_set
# it will look in set 1 and then remove the items from the 2nd set (would show 1,2,3)
#
# Sets don't allow duplicates, can do subtraction and addition, union, min, max, len, and doesn't support indexing
# Where order isn't important, but should be unique, use set

#dictionaries
#class is dict and uses key value pairs
# occurrances = dict(a=5, b=6, c=8)
# #{'a': 5, 'b': 6, 'c': 8}
#
# type(occurrances) ia class 'dict'
#
# in a dictionary, it's not indexes based on order, but the key value' \
#
# occurrances['d'] = 15
# occurrances
# {'a': 5, 'b': 6, 'c': 8, 'd': 15}
#
# occurrances['d'] = 10
# occurrances['d']
#
# #if you try to get a value that doesn't exist will give a stdin error'
# occurrances['e']
#
# occurrances.get('e') #would return none
# occurrances.get('e', 10) #would return the default of 10
#
# occurrances.keys()  #dict_keys(['a', 'b', 'c', 'd'])
# occurrances.values()    #dict_values([5, 6, 8, 10])
# occurrances.items() #dict_items([('a', 5), ('b', 6), ('c', 8), ('d', 10)]) <-list of tuples, key:value
#
# for (key,value) in occurrances.items():
#     print(f"{key} {value}")
#
# can delete
# occurrances['a']=0 will set the value to 0
# del occurrances['a'] will delete the key-value pair

#squares_first_ten_numbers = [ i*i for i in range(1,11) ]
#type(squares_first_ten_numbers)
#<class 'list>'

# squares_first_ten_numbers_set = set(squares_of_first_10_numbers)
# squares_first_ten_numbers_set = {i*i for i in range(1,11)}
# type(squares_first_ten_numbers_set)
# <class 'set'>
# print(squares_first_ten_numbers_set)

#squares_first_ten_numbers_dict = {i: i*i for i in range(1,11)}
#type(squares_first_ten_numbers_dict)
#<class 'dict'>

# type([])
# type({})
# type(set())
#
# type({1})
# type({'A':5})
# type(())

def create_ranga():
    return 'Ranga',1981,'India'


ranga = create_ranga()
type(ranga)

name, year, country = ranga
print(name)
print(year)
print(country)

ranga[0]
ranga[1]
ranga[3]

#once created, the values are immutable.  Tuples are more efficient if the data is static


