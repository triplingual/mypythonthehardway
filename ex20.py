from sys import argv
import os

script, input_file = argv

def print_all( f ):
	print f.read()

def rewind( f ):
#	f.seek( 0 )
# get to the beginning in a roundabout way, just for fun
# NB: for some reason, at this point the variable f represents 
#     a file rather than a string, so we have to go back and get the string name
	size = os.path.getsize( f.name )
	f.seek( 0 - size, 2 )

def print_a_line( line_count, f ):
	print line_count, f.readline()

current_file = open( input_file )

print "First let's print the whole file:"
print_all( current_file )

print "Now let's rewind, kind of like a tape.\n"
rewind( current_file )

print "Let's print three lines:"

current_line = 1
print_a_line( current_line, current_file )

current_line += 1
print_a_line( current_line, current_file )

current_line += 1
print_a_line( current_line, current_file )
