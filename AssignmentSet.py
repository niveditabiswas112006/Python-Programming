# Write a Python program to remove an item from a set if it is present in the set.


"""
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}


item_to_remove = 3
item_to_remove = 6
item_to_remove = 9


if item_to_remove in my_set:
   my_set.remove(item_to_remove)


print("Updated set:", my_set)

"""


# Write a Python program to check if two given sets have no elements in common.


"""
set1 = {1, 2, 3}
set2 = {4, 5, 6}


if set1.isdisjoint(set2):
   print("The two sets have no elements in common.")
else:
   print("The two sets have elements in common.")

"""


# Write a Python program toGet Only unique items from two sets


"""
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


unique_items = set1.symmetric_difference(set2)


print("Unique items from both sets:", unique_items)

"""


# Write a Python program to Convert Set to one String


"""
my_set = {'apple', 'banana', 'cherry'}

result_string = ', '.join(my_set)

print("Set as a string:", result_string)

"""

# program to count number of vowels using sets in given string

"""
input_string = "Hello, how was your day?"

vowels = set("aeiou")

vowel_count = sum(1 for char in input_string if char in vowels)

print("Number of vowels in the given string:", vowel_count)

"""



