# Exercise 38: Doing things to lists.

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, there are not ten things in that list.  Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff [-1] # Whoah.  Fancy!
print stuff.pop()
print ' '.join(stuff) # What happen?!  Main screen turn on!
print ' ' .join(stuff[3:5]) # For great justice!