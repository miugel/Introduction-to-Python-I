# experiment with scopes in Python
# good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# when you use a variable in a function, it's local in scope to the function

x = 12

def change_x():
    global x
    x = 77

change_x()

# this prints 12, what do we have to modify in change_x() to get it to print 99?

print(x)

# this nested function has a similar problem

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # this prints 120, what do we have to change in inner() to get it to print 999?
    # note: Google 'python nested function scope'
    
    print(y)

outer()