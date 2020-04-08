# for this exercise, look up the methods and functions that are available for use with Python lists

x = [1, 2, 3]
y = [8, 9, 10]

# for the following, DO NOT USE AN ASSIGNMENT (=)

# change x so that it is [1, 2, 3, 4]

x.append(4)
print(x)

# using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]

for item in y:
    x.append(item)
print(x)

# change x so that it is [1, 2, 3, 4, 9, 10]

x.remove(8)
print(x)

# change x so that it is [1, 2, 3, 4, 9, 99, 10]

x.insert(5, 99)
print(x)

# print the length of list x

print(len(x))

# print all the values in x multiplied by 1000

for item in x:
    print(item * 1000)