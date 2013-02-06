def user_input_test(arg1, arg2):
	print "Arg value = %r" % arg1
	print "Arg value = %r" % arg2

print "METHOD 1"
print "Enter a value: "
datum1 = raw_input("> ")
print "Enter another value: "
datum2 = raw_input("> ")
user_input_test(datum1, datum2)

print "\nMETHOD 2"
user_input_test("value 1", "value 2")

print "\nMETHOD 3"
# uses stdin values from above
user_input_test(datum1 + ", value 1", datum2 + ", value 2")

print "\nMETHOD 4"
input = open("quxes.txt")
datum1 = input.readline()
datum2 = input.readline()
user_input_test( datum1, datum2 )

print "\nMETHOD 5"
# uses values from above file open method
print "Enter a value: "
input1 = raw_input("> ")
print "Enter another value: "
input2 = raw_input("> ")
user_input_test( datum1 + ", " + input1, datum2 + ", " + input2 )

print "\nMETHOD 6"
# uses values from above file open method
# uses stdin values from second intake above
user_input_test( datum1 + ", " + input1 + ", and the next", datum2 + ", " + input2 + ", and the rest" )

print "\nMETHOD 7"
# uses values from above file open method, then concatenates with a second file
newfile = open("killfile.txt")
datum3 = newfile.readline()
datum4 = newfile.readline()
user_input_test( datum1 + ", " + datum3, datum2 + ", " + datum4 )

print "\nMETHOD 8"
# uses values from first file open method above and then does math
user_input_test( datum1 + ", " + str(2*2), datum2 + ", " + str(5*4) )

print "\nMETHOD 9"
# compares user input to fixed value
print "Enter a value: "
user_input_1 = raw_input("> ")
print "Enter another value: "
user_input_2 = raw_input("> ")
user_input_test(user_input_1 == "foo", user_input_2 == "bar")

print "\nMETHOD 10"
# establishes non-zero length user input
print "Enter a value: "
user_input_1 = raw_input("> ")
print "Enter another value: "
user_input_2 = raw_input("> ")
user_input_test(len(user_input_1) >= 0, len(user_input_2) >= 0)
