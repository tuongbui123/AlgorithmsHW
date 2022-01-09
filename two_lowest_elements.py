
import sys

def print2Smallest(arr):

    arr_size = len(arr)
    if arr_size < 2:
        print ("Invalid Input")
        return

    first = second = sys.maxsize
    for i in range(0, arr_size):

        # If current element is smaller than first then
        # update both first and second
        if arr[i] < first:
            second = first
            first = arr[i]

        # If arr[i] is in between first and second then
        # update second
        elif (arr[i] < second and arr[i] != first):
            second = arr[i]

    if (second == sys.maxsize):
        print ("No second smallest element")
    else:
        print ('The smallest element is',first,'and' 
              ' second smallest element is',second)

# Driver function to test above function
arr = [198, 3, 4, 9, 10, 9, 2]
print2Smallest(arr)