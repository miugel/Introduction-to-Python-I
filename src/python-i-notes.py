name = 'Miguel'
print(name)

# four data types, string, int, float, boolean
# strings and integers cannot be concatenated
# integers and floats can be concatenated

# arrays in python are called lists

list = [1, 2, 3, 4]

for i in list:
    print(i)

# indentation is very important
# cannot mix tabs and spaces, pick one or the other

for i in range(5):
    print(f'this is the {i}th time')

for i, e in enumerate(list):
    print(i, e)

# repl, mini text editor, by just typing python3, etc.
# help(something goes in here), data type

# LIST COMPREHENSIONS

# only use is when comparing to 'none'

# these two do the same thing
evens = []

for num in range(10):
    if num % 2 == 0:
        evens.append(num)

print(evens)

evens = [num for num in range(10) if num % 2 == 0]

print(evens)

# can leave off off of conditional in list comprehension
# can chain conditionals with 'and'

# DICTIONARIES

dictionary = {'fruit': 'mango', 'fat': 'dog'}

for key in dictionary:
    print(key)
    print(dictionary[key])

for key, value in dictionary.items():
    print(f'{key}: {value}')