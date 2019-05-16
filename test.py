def show(name):
	print(f'Przed modyfikacją:{name}')
	name[0]='Beata'
	name[1]='Barbara'
	name[2]='Bogdan'
	print(f'Po modyfikacji:{name}')

data = ['Anna','Agnieszka','Andrzej']

print(f'Przed wywołaniem funkcji show:{data}')

show(data)

#Przekazywanie argumentów przez wartość

print('\n\n')

def show1(city):
	print(f'Przed modyfikacją:{city}')
	city[0]='Berlin'
	city[1]='Bukareszt'
	print(f'Po modyfikacji:{city}')

miasto = ['Poznań','Gniezno']
print(f'Przed wywołaniem funkcji show1:{miasto}')
show1(list(miasto))
print(f'Po wywołaniu funkcji:{miasto}')



print('\n\n')

### SŁOWNIK ###

def show2(data1):
	print(f'Przed modyfikacją:{data1}')
	name[0] = 'Beata'
	name[1] = 'Barbara'
	name[2] = 'Bogdan'
	print(f'Po modyfikacji:{data1}')

slownik = {
	0:'Artur',
	1:'Andrzej'
}
#1
print(f'Przed wywołaniem funkcji show:{slownik}')

show(dict(slownik))

#2
print(f'Po funkcji show2:{slownik}')
