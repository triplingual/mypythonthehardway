# Echoing a well-known nursery rhyme to stdout
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
# Oh, wait, it's a twist!
print "." * 10 # what'd that do?

# Composing word(s) letterwise
end1 = "C"
end2 = 'h'
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B" # note change in capitalization
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# illustrating one way to make code reader-friendly
# watch that comma at the end. Try removing it to see what happens.
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
