# 1) print out the value for the key 'history' using the dictionary below


sampleDict = {
    "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
}
# everything before dictionary is name so need to include everything before curly bracate

# print(sampleDict)
# history_value = sampleDict["history"]
# print(history_value)
print(sampleDict["class"]["student"]["marks"]["history"])



# 2) Add 2 inches to the son's height.

dict = {
    "son's name": "Lucas",
    "son's eyes": "green",
    "son's height": 32,
    "son's weight": 25,
}
dict["son's height"] = int(dict["son's height"]) + 2 #this will simply update with other remain the same
#you can remove the int( part but its good to have 
print(dict)

# son_height = dict["son's height"]+2 #this will just give you son's height 
# print(son_height)
                  

# 3) Given a Python dictionary, Change Brad’s salary to 8500

sampleDict = {
    "emp1": {"name": "Jhon", "salary": 7500},
    "emp2": {"name": "Emma", "salary": 8000},
    "emp3": {"name": "Brad", "salary": 6500},
}

sampleDict["emp3"]["salary"] = 8500 #if you want to change salary 
print(sampleDict)

# sampleDict["emp3"]["name"]= "Pitt" #if you want to change name 
# print(sampleDict)



# 4 )Given the dictionary below, add a new key - 'work' with the values shown below:
#       "work": ["Apology", "Phaedo", "Republic", "Symposium"]

dict = {
    "name": "Plato",
    "country": "Ancient Greece",
    "born": -427,
    "teacher": "Socrates",
    "student": "Aristotle",
}

# dict["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]
# print(dict)

dict["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]
print(dict)
