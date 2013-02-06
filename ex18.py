# this one is like a script with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# since *args is pointless, we can enumerate the args required
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Trip", "Kirkpatrick")
print_two_again("Trip", "Kirkpatrick")
print_one("First!")
print_none()
