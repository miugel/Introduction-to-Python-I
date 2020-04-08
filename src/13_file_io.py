"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# open up the 'data.txt' file (which already exists) for reading
# print all the contents of the file, then close the file
# note: pay close attention to your current directory when trying to open 'data.txt'

import os
directory = os.getcwd()
data = open(f'{directory}\src\data.txt', 'r')
print(data.read())
data.close()

# open up a file called 'bar.txt' (which doesn't exist yet) for writing
# write three lines of arbitrary content to that file, then close the file
# open up 'bar.txt' and inspect it to make sure that it contains what you expect it to contain

bar = open('src/bar.txt', 'w+')
bar.write('first line\n')
bar.write('second line\n')
bar.write('third line\n')
bar.close()

# need directory in one but not the other?