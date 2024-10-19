#Write a Python program to reverse the order of the items in the array.

"""
def reverse_array(arr):
    return arr[::-1]

if __name__ == "__main__":
    original_array = [1, 2, 3, 4, 5]
    print("Original array:", original_array)
    reversed_array = reverse_array(original_array)
    print("Reversed array:", reversed_array)
    
"""


#Write a Python program to get the number of occurrences of a specified element in an array.

"""def count_occurrences(arr, element):
    count = 0
    for item in arr:
        if item == element:
            count += 1
    return count

if __name__ == "__main__":
    array = [1, 2, 3, 4, 2, 5, 2]
    element_to_count = 2
    print("Array:", array)
    occurrences = count_occurrences(array, element_to_count)
    print(f"The element {element_to_count} occurs {occurrences} times in the array.")

"""


# Write a Python program to find out if a given array of integers contains any duplicate elements.

"""
def contains_duplicates(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 2]
    print("Array:", array)
    if contains_duplicates(array):
        print("The array contains duplicates.")
    else:
        print("The array does not contain duplicates.")

"""


# Write a  Python program to find the missing number in a given array of 5 continuous numbers.

"""
def find_missing_number(arr):
    n = 5
    expected_sum = (min(arr) + max(arr)) * n // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

if __name__ == "__main__"
    array = [3, 4, 5, 1]
    print("Array:", array)
    missing_number = find_missing_number(array)
    print(f"The missing number is: {missing_number}")

"""


# Replace all odd numbers in the given array with -1

"""
def replace_odd_with_negative_one(arr):
    return [-1 if num % 2 != 0 else num for num in arr]

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Original array:", array)
    modified_array = replace_odd_with_negative_one(array)
    print("Modified array:", modified_array)
    
"""

