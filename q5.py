# 5. Swap Two Variables
# Prompt for two variables and swap their values. Show the results before and after swapping.

a=input("Enter the 1st variable (a): ")
b=input("Enter the 2nd variable (b): ")

print(f"Before swapping: a={a}, b={b}")
a,b=b,a
print(f"After swapping: a={a}, b={b}")
