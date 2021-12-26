s = "AutomationQAtesting"

# printing original string
print("The original string is : " + s)

# Using string slicing
# Splitting string into equal halves
first_half = s[len(s)//2:]
second_half = s[:len(s)//2]

# printing result
print("The first part of string : " + first_half)
print("The second part of string : " + second_half)