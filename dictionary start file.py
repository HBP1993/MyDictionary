#it is the dictionary of phone number and key is Chris and crossponding value is phone number 
phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


# print()
# print('*****  start section 1 - print dictionary ********')
# print()

# print(phonebook) #this print the phonebook

# print(len(phonebook)) #this prints the length of phonebook i.e. 3

# print(type(phonebook))  #this printa the type of the object i.e. dict

# mydictionary = dict(m=8, n=9) #another way to create the dictionary
# print(mydictionary)


# #with the list you get the particular element with the help of index value
# #with the ductionaries we have to give it a key and we get return back the value 

# chris_phone = phonebook['Chris'] #calling the dictionary and giving key
# print(chris_phone) #return the crossponding phonenumber 

# #when the key is not in the dictionary it gives the key error and it is case sentitive
# print()
# print('*****  end section 1 ********')
# print()



# print()
# print('*****  start section 2 - search dictionary ********')
# print()

# name = 'Chris'
# #rather than getting key error we can use the end method to track if certain elements are
# #in dictionary 

# if name in phonebook:
#     print(phonebook[name])
    
# else:
#     print(name,"is not found in phonebook.")


# print()
# print('*****  end section 2 ********')
# print()




# print()
# print('*****  start section 3 - edit/append dictionary ********')
# print()
# #dictionary are also mutable objects like the list that means we can alter the content 
# phonebook['Joe'] = '555-0123' #if key doesn't exit in dictionary it automatically added to dictionary
# phonebook['Chris'] = '555-4444' #if key exist in the dictionary it change the key value    

# print(phonebook) 






# print()
# print('*****  end section 3 ********')
# print()






# print()
# print('*****  start section 4 - delete/remove from dictionary ********')
# print()

# del phonebook ['Chris']

# print(phonebook)


# print()
# print('*****  end section 4 ********')
# print()





# print()
# print('*****  start section 5 - iterate through keys ********')
# print()

# #just like any other obejct you need to be able to go through all the elements because you may have
# #the operation you need to perform each elements in that object so dictionary are no different than list 

# for key in phonebook: #whenever we iterate through dictionary is gonna iterate through key automatically
# #key is just a variable here we can name any variable in place of key like i in phonebook
#     print(key)
#     print(phonebook[key]) #here we just want value of key   

    


# print()
# print('*****  end section 5 ********')
# print()






# print()
# print('*****  start section 6 - iterate through values  ********')
# print()

# for value in phonebook.values():    #here have is the method of dictionary object
# #function that is particular to an object is called method
#     print(value)


# print()
# print('*****  end section 6 ********')
# print()




# print()
# print('*****  start section 7 - iterate through both key and value pair********')
# print()

# for phonebook_tuple in phonebook.items(): #it gives key and value in pair
#     print(phonebook_tuple)
#     print(type(phonebook_tuple))

# for key, value in phonebook.items(): #instead of using one variable if we use two variable
#     #it gives you value saperately 
#     print(key)
#     print(value)


# print()
# print('*****  end section 7 ********')
# print()


# print()
# print('*****  start section 8 - using get and clear methods ********')
# print()

# #if the key doesnot exist we get key error and it breaks our program
# #get method allows you to give it two arguments one is key that you looking for and another is 
# #defult value if it doesn't find the key 

# phone = phonebook.get("Chris", 'key not found')

# print(phone)

# phonebook.clear() #it removes all the elements from the dictionary rather than deleting

# print(phonebook) #this will give the empty dictionary



# print()
# print('*****  end section 8 ********')
# print()


# print()
# print('*****  start section 9 - using pop and popitems ********')
# print()
#pop method removes the key value pairs from the dictionary. it does allow you to get defult function

#this key value pair will be in remove and phonebook have no longer that value 
#it is different than delete, delete completely remove 

#remove = phonebook.pop('Chris', 'not found')

#print(remove)

#print(phonebook)

#in popitem method you get the key value pair together but the problem is that it just
#ramdomize or random key have pair from dictonary and pop it out

# a = phonebook.popitem()

# print(a)

# print(phonebook)



# print()
# print('*****  end section 9 ********')
# print()






import random
print()
print('*****  start section 10 - using random and converting to list ********')
print()

#inorder be able to fix that we use random and convert to list 
#using the list function you can create the randomize the key 

# random_keys = list(phonebook) #this converts the list 
# print(random_keys) 

#nested choice in one line 
random_phone = phonebook[random.choice(list(phonebook))]
print(random_phone)


# choice = random.choice(random_keys) #this picks random key
# print(choice)

# print(phonebook[choice]) #this picks random choice


print()
print('*****  end section 10 ********')
print()





