# Write a Python program to compute the element-wise sum of given tuples.           
# Original : (1, 2, 3, 4)   (3, 5, 2, 1)   (2, 2, 3, 1)
# Element-wise sum of the said tuples:  (6, 9, 8, 6)

"""
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)


elementwise_sum = tuple(sum(values) for values in zip(tuple1, tuple2, tuple3))


print("Original:", tuple1, tuple2, tuple3)
print("Element-wise sum of the said tuples:", elementwise_sum)

"""


# Write a Python program to convert a given list of tuples to a list of lists.
# Original list of tuples: [(1, 2), (2, 3), (3, 4)]

"""
original_list = [(1, 2), (2, 3), (3, 4)]


list_of_lists = [list(tup) for tup in original_list]


print("Original list of tuples:", original_list)
print("Converted list of lists:", list_of_lists)

"""


# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]


"""
original_list = [(1, 2), (2, 3), (3, 4)]

list_of_lists = [list(tup) for tup in original_list]

print(list_of_lists)

"""


# Write a Python program to remove an empty tuple(s) from a list of tuples.

"""
original_list = [(1, 2), (), (3, 4), (), (5,6)]


filtered_list = [tup for tup in original_list if tup]


print("Original list of tuples:", original_list)
print("List after removing empty tuples:", filtered_list)

"""


# Write a Python program to convert a given string to a tuple# Given string


"""
input_string = "Apple, Banana, Cherry, strawberry, Avocado, Guava, Coconut"


tuple_result = tuple(item.strip() for item in input_string.split(','))


print("Original string:", input_string)
print("Converted tuple:", tuple_result)

"""


# Write a Python program to calculate the product, multiplying all the numbers in a given tuple.


"""
numbers_tuple = (1, 2, 3, 4, 5,6,7,8)


product = 1


for number in numbers_tuple:
   product *= number


print("Given tuple:", numbers_tuple)
print("Product of all numbers:", product)

"""



