# Assign numbers to variables
i = 3
j = 2
k = i - j
print "k = ", k

x = (i + j) * (i + j)
print "x = ", x
y = (i + j) * i * j
print "y = ", y
z = (i * j)
print "z = ", z


# Declare intent
print "I will now count my chickens:"

# Calculate number of hens
print "Hens", x + y / z
# Calculate number of roosters, rounded to the nearest whole number
print "Roosters", 100 - x * 3 % 4

# Declare intent to count eggs
print "Now I will count the eggs:"

# Long string of arithmatical operations resulting in number of eggs rounded to nearest whole number
print i + j + k - 5 + 4 % j - k / 4 + z

# Introduction to comparison operations
# Declaration of intent
print "Is it true that 3 + 2 < 5 - 7?"

# Calculate T/F using math
print i + j < (i + j) - 7

# Breakdown of comparison sides
print "What is 3 + 2?", i + j
print "What is 5 - 7?", (i + j) - 7

# Witty comment
print "Oh, that's why it's False."

# Interrogative masquerading as a declarative
print "How about some more?"

# Further mathematical comparisons
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
