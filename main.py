from person import Person

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)

jordan.greet(sonny)

print(f' name: {sonny.email}\n phone {sonny.phone}')

print(f' name: {jordan.email}\n phone {jordan.phone}')

jordan.add_friend(sonny)