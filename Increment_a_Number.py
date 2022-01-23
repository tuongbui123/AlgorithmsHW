
def incrementVector(a):
    n = len(a)

    # Add 1 to last digit and find carry
    a[n - 1] += 1
    carry = a[n - 1] / 10
    a[n - 1] = a[n - 1] % 10

    # Traverse from second last digit
    for i in range(n - 2, -1, -1):
        if (carry == 1):
            a[i] += 1
            carry = a[i] / 10
            a[i] = a[i] % 10

    # If carry is 1, we need to add
    # a 1 at the beginning of vector
    if (carry == 1):
        a.insert(0, 1)


mylist = []
# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    elements = int(input())

    mylist.append(elements)

incrementVector(mylist)

print(mylist)
