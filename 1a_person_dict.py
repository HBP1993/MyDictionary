person = {}  # empty dictionary

# adding key value pairs values with strings, int, list, and dictionary
#dictionary is collection of anything 'sky is the limit'
person["fname"] = "Joe"  
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
#when you dealing with the list you need index of that value 
person["children"] = ["Ralph", "Betty", "Joey"] #list
#when you dealing with the dictionary you need key of that value 
person["pets"] = {"dog": "Fido", "cat": "Sox"}   #dictionary

# pets is a another dictionary value

#print(person)

#print(type(person["children"]))


print(person["children"][1]) #if you want to print betty 


print(person["pets"]["cat"]) #dealing dictionary within the dictionary; it will print Sox


for i in person["children"]: #if we want to iterate through all the children 
    print(i)  # i is list and it is iterater 

for i, j in person["pets"].items():
    print(i) #
