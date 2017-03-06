my_name = 'Alex T. Taxter'
my_age = 22 # Honest truth
my_height = 187 # centimetres
my_weight = 72.9 # kilograms
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Blonde'

print "Let's talk about %s." % my_name
print "He's %d centimetres tall." % my_height
print "He's about %d kilograms in weight." % my_weight
print "Actually, that is not that heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This next line is tricky, try to get it exactly right.

print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)