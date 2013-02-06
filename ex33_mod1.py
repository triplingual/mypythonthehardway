import random

def looper( param0, param1 ):
	"""Loops"""
	i = 0
	numbers = []
	while i < param0:
		if ( i < ( 2 * param1 ) ):
			print "At the top i is %d" % i
		numbers.append( i )
		i = i + param1
		if ( i < ( 2 * param1 + 1 ) ):
			print "Numbers now: ", numbers
			print "At the bottom i is %d" % i
	return numbers

numbers = looper( 6, 1 )

print "The numbers: "
for num in numbers:
	print num

limit = 1000
increment = 10
numbers = looper( limit, increment )

# one way to deal with a large set
print "The numbers: "
for num in numbers:
	slash = random.choice( '/\\\|' )
	if num > ( limit - ( 2 * increment ) ) or num < 2 * increment :
		print num
	elif num == ( limit - ( 2 * increment ) ):
		print slash
	else:
		print slash,

