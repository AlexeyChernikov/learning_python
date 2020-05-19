import shelve


class TestClass:
    pass


vegetables_list = ['tomato', 'potato', 'carrot']
fruits_tuple = ('pineapple', 'banana', 'apple')
countries_dict = {'Russia': 'Moscow', 'UK': 'London', 'China': 'Beijing'}

s = shelve.open("test")
s["vegetables"] = vegetables_list
s["fruits"] = fruits_tuple
s["countries"] = countries_dict
s["int_item"] = 1
s["bool_item"] = True
s["strint_item"] = 'test string'
s["class_item"] = TestClass()
s["shelve"] = s
s.close()

print()

s = shelve.open("test")
print('Sequences:')
print('Vegetables list:', s["vegetables"])
print('Fruits tuple:', s["fruits"])
print('Countries dictionary:', s["countries"])

print('\nIndividual items:')
print(s["vegetables"][0])
print(s["fruits"][0])
print(s["countries"]["Russia"])
print(s["shelve"])

print('\nActions with shelves:')
print('Shelve keys:', [value for value in s.keys()])
print('\nShelve values:', [value for value in s.values()])
print('\nShelve items:', [value for value in s.items()])

del s["vegetables"]
print('\nDelete vegetables list:', [value for value in s.items()])

s["int_item"] = 100
print('\nChange "int_item" value:', s["int_item"])

print('\nShelve in shelve:')
print(s["shelve"]["vegetables"])

s.clear()
print('\nShelve now:', [value for value in s.items()])
s.close()