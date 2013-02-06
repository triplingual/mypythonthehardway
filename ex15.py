# include modules
from sys import argv

# assign variables to args
script, filename = argv

# obtain file object
txt = open(filename)

# pull input filename into a literal representation and print, print file contents
print "Here's your file %r:" % filename
print txt.read()

# get file name again from user and put it into a new variable
print "Type the filename again:"
file_again = raw_input("> ")

# get a new file object
txt_again = open(file_again)

# print out file contents
print txt_again.read()
