#create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'NY'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#do it by using the states then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}.")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")

#safely get an abbreviation that might not be there
print('-' * 10)
states = states.get('Texas')
if not state:
	print("Sorry, no Texas.")

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state of 'TX' is: {city}")

favorite_things = {}
favorite_things["number"] = 3
favorite_things["color"] = "blue"
favorite_things["taco"] = "Bean n Cheese"
favorite_things["pets"] = []
favorite_things["pets"].append("Sora")
favorite_things["pets"].append("Machi")
print(favorite_things)