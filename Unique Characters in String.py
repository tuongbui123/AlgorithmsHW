
def uniqueCharacters(str):
    # If at any time we encounter 2
    # same characters, return false
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if (str[i] == str[j]):
                return False;
    return True;


str = input("Please enter a string: ")

if (uniqueCharacters(str)):
    print("The String ", str, " has all unique characters");
else:
    print("The String ", str, " has duplicate characters");

