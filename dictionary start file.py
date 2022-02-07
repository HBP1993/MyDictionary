from random import choice


phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

'''
print()
print("*****  start section 1 - print dictionary ********")
print()


print(phonebook)

print(len(phonebook))
print(type(phonebook))

mydictionary = dict(m=8, n=9)
print(mydictionary)

chris_phone = phonebook("Chris")
print(chris_phone)

print()
print("*****  end section 1 ********")
print()

'''


print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'chris'

if name in my phonebook:
    print(phonebook[name])
else:
    print('name not found')



print()
print('*****  end section 2 ********')
print()




"""


print()
print("*****  start section 3 - edit/append dictionary ********")
print()

phonebook["joe"] = "555-0123"
phonebook["Chris"] = "555-4444"
# added and updated

print(phonebook)


print()
print("*****  end section 3 ********")
print()

"""





print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del.phonebook['Chris']

print(phonebook)



print()
print('*****  end section 4 ********')
print()


"""


print()
print("*****  start section 5 - iterate through keys ********")
print()

for key in phonebook:
    print(key)
    print(phonebook[key])


print()
print("*****  end section 5 ********")
print()


print()
print("*****  start section 6 - iterate through values  ********")
print()

for value in phonebook.values():
    # funtion in a particular object is method
    print(value)


print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - iterate through both key and value pair********")
print()

for phonebook_tuple in phonebook.items():
    print(phonebook_tuple)
    print(type(phonebook_tuple))


for key, value in phonebook.items():
    print(key)
    print(value)


print()
print("*****  end section 7 ********")
print()

"""

print()
print('*****  start section 8a - using get and clear method ********')
print()


phone = phonebook.get('Chris', 'key not found')
print(phone)

phonebook.clear()

print(phonebook)



print()
print('*****  end section 8a ********')
print()

"""
print()
print("*****  start section 9a - using pop and popitem ********")
print()

# remove = phonebook.pop("Chris", "not found")

# print(remove)

# print(phonebook)

a = phonebook.popitem()

print(a)

print(phonebook)

"""

print()
print('*****  end section 9a ********')
print()



"""

import random

print()
print("*****  start section 10 - using random and converting to list ********")
print()

#randon_keys = list(phonebook)
#print(random_keys)

#choice = random.choice(random_keys)
#print(choice)

#print(phonebook[choice])



randon_keys = phonebook[random.choice(list(phonebook))}
print(random_keys)

choice = random.choice(random_keys)
print(choice)

print(phonebook[choice])


print()
print("*****  end section 10 ********")
print()
