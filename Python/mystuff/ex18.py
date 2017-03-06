# This is just like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# Okay, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# This just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# This one is a strong independent function that takes no arguments
def print_none():
	print "You don' own me - mmmmhm"

print_two("Alex", "Taxter")
print_two_again("Alex", "Taxter")
print_one("First!")
print_none()