import pickle

vegetables_list = ['tomato', 'potato', 'carrot']
fruits_tuple = ('pineapple', 'banana', 'apple')
countries_dict = {'Russia': 'Moscow', 'UK': 'London', 'China': 'Beijing'}
shelve_imitation = {'vegetables': vegetables_list, 'fruits': fruits_tuple, 'countries': countries_dict}

print('Work with separate structures:')

f = open("test.dat", "wb")
pickle.dump(vegetables_list, f)
pickle.dump(fruits_tuple, f)
pickle.dump(countries_dict, f)
f.close()

f = open("test.dat", "rb")
vegetables = pickle.load(f)
fruits = pickle.load(f)
countries = pickle.load(f)

print('Sequences:')
print('Vegetables list:', vegetables)
print('Fruits tuple:', fruits)
print('Countries dictionary:', countries)

print('\nIndividual items:')
print(vegetables[0])
print(fruits[1])
print(countries['China'])
f.close()

print('\nShelve imitation:')

f = open("test1.dat", "wb")
pickle.dump(shelve_imitation, f)
f.close()

f = open("test1.dat", "rb")
shelve = pickle.load(f)

print('Sequences:')
print('Vegetables list:', shelve['vegetables'])
print('Fruits tuple:', shelve['fruits'])
print('Countries dictionary:', shelve['countries'])

print('\nIndividual items:')
print(shelve['vegetables'][0])
print(shelve['fruits'][1])
print(shelve['countries']['China'])

print('\nActions with shelves:')
print('Shelve keys:', [value for value in shelve.keys()])
print('Shelve values:', [value for value in shelve.values()])
print('Shelve items:', [value for value in shelve.items()])
f.close()