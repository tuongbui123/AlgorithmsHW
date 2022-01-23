def even_odd(arr):
    next_even = 0
    next_odd = len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            if arr[next_odd] % 2 == 0:
                arr[next_odd], arr[next_even] = arr[next_even], arr[next_odd]
                next_even += 1
                next_odd -= 1
            else:
                next_odd -= 1
    return arr


mylist = []
# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    elements = int(input())

    mylist.append(elements)

print(even_odd(mylist))
