import hashmap

# Create a mapping of state to abbreviation.
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# Create a basic set of states and some cities in them.
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# Add some more cities.
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# Print out some cities.
print '-' * 10
print "NY state has: %s" % hashmap.get(cities, 'NY')
print "OR state has: %s" % hashmap.get(cities, 'OR')

# Print out some states.
print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

# Print every state abbreviation.
print '-' * 10
hashmap.list(states)

# Print every city in state.
print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, no Texas.  Good."
    
# Default values using //= with the nil result
# Can you do this in one line?
city = hashmap.get(cities, 'TX', 'Does not exist')
print "The city for the state 'TX' is: %s" % city