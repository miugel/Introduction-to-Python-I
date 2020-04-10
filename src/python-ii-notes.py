# warmup

def my_function(a):
    a[0] = 99

a = [0, 1, 2, 3, 4]
my_function(a)
print(a)

# does the function refer to the original variable or a copy?
# almost like it creates copy

# BUT, it modifies the original list
# some types are passed by reference, like lists, dictionaries, and sets, and others by value, like variables
# pass/call by sharing
# can figure out if two variables are using the same value in memory with the is operator
# interred values only have one copy in memory
# numbers bigger than 256 and strings with punctuation have more than one copy
# when no more variables map to something, python can dispose of it and free memory