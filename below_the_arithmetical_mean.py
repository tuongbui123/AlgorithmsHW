import statistics


mylist = [1, 3, 5, 6, 4, 10, 2, 3]

x = statistics.mean(mylist)

y = [n for n in mylist if n < x]

print(y)