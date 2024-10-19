# Write a Python program to remove duplicates from a list.

"""
def remove_duplicates(input_list):
   seen = set()
   result = []
   for item in input_list:
       if item not in seen:
           seen.add(item)
           result.append(item)
   return result


input_list = [1, 2, 2, 3, 4, 4, 5]
output_list = remove_duplicates(input_list)
print("Original list:", input_list)
print("List after removing duplicates:", output_list)

"""


# Write a Python function that takes two lists and returns True if they have at least one common member.

"""
def have_common_member(list1, list2):


   set2 = set(list2)


   for item in list1:
       if item in set2:
           return True
   return False




list_a = [1, 2, 3, 4]
list_b = [4, 5, 6, 7]
list_c = [8, 9, 10]


print(have_common_member(list_a, list_b))
print(have_common_member(list_a, list_c)) 

"""


# Write a Python program to print the numbers of a specified list after removing even numbers from it.

"""
def remove_even_numbers(input_list):


   odd_numbers = [num for num in input_list if num % 2 != 0]
   return odd_numbers




specified_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even_numbers(specified_list)


print("Original list:", specified_list)
print("List after removing even numbers:", result)

"""


# Write a Python program to find the second smallest number in a list.

"""
def find_second_smallest(input_list):
   if len(input_list) < 2:
       return None


   smallest = float('inf')
   second_smallest = float('inf')


   for num in input_list:
       if num < smallest:
           second_smallest = smallest
           smallest = num
       elif smallest < num < second_smallest:
           second_smallest = num


   return second_smallest if second_smallest != float('inf') else None


specified_list = [5, 3, 1, 2, 4, 1, 3]
second_smallest = find_second_smallest(specified_list)


if second_smallest is not None:
   print("The second smallest number is:", second_smallest)
else:
   print("There are not enough unique numbers to determine the second smallest.")

"""


# Write a Python program to split a list every Nth element.

"""
def split_list_every_nth(input_list, n):
   if n <= 0:
       raise ValueError("N must be a positive integer.")
  


   return [input_list[i:i + n] for i in range(0, len(input_list), n)]


specified_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
result = split_list_every_nth(specified_list, n)


print("Original list:", specified_list)
print(f"List split every {n} elements:", result)

"""


# Write a Python a function to find the union and intersection of two lists.

"""
def find_union_and_intersection(list1, list2):


   set1 = set(list1)
   set2 = set(list2)
   union = set1 | set2
   intersection = set1 & set2
   return list(union), list(intersection)
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]


union, intersection = find_union_and_intersection(list_a, list_b)


print("Union of the two lists:", union)
print("Intersection of the two lists:", intersection)

"""


# Write a Python function to check if a list is a palindrome or not. Return true otherwise false.

"""
def is_palindrome(input_list):
   return input_list == input_list[::-1]
specified_list = [1, 2, 3, 2, 1]
result = is_palindrome(specified_list)


if result:
   print("The list is a palindrome.")
else:
   print("The list is not a palindrome.")

"""


