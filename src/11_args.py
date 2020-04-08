# experiment with positional arguments, arbitrary arguments, and keyword arguments

# write a function f1 that takes two integer positional arguments and returns the sum, this is what you'd consider to be a regular, normal function

def f1(num1, num2):
    return num1 + num2

print(f1(1, 2))

# write a function f2 that takes any number of integer arguments and prints the sum
# note: Google for 'python arbitrary arguments' and look for '*args'

def f2(*argv):
    for arg in argv:
        print(arg)


print(f2(1))                    # should print 1
print(f2(1, 3))                 # should print 4
print(f2(1, 4, -12))            # should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # should print 33

a = [7, 6, 5, 4]

# how do you have to modify the f2 call below to make this work?

print(f2(*a))    # should print 22

# write a function f3 that accepts either one or two arguments, if one argument, it returns that value plus 1. If two arguments, it returns the sum of the arguments
# note: Google 'python default arguments' for a hint

def f3(num1, num2 = 1):
    return num1 + num2

print(f3(1, 2))  # should print 3
print(f3(8))     # should print 9

# write a function f4 that accepts an arbitrary number of keyword arguments and prints out the keys and values like so:
# key: foo, value: bar
# key: baz, value: 12
# note: Google 'python keyword arguments'

def f4(**kwargs):
    for key, value in kwargs.items():
        print(f'key: {key}, value: {value}')

# should print
# key: a, value: 12
# key: b, value: 30

f4(a=12, b=30)

# should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: 'March 23, 1868'

f4(city='Berkeley', population=121240, founded='March 23, 1868')

d = {
    'monster': 'goblin',
    'hp': 3
}

# how do you have to modify the f4 call below to make this work?

f4(**d)