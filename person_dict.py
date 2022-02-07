person = {}  # empty dictionary
person["fname"] = "Joe"  # adding values
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}
# pets is a another dictionary value


# print(person["children"])


print(person["children"][1])


print(person["pets"]["cat"])
# dictionary within the dictionary

for i in person["children"]:
    print(i)

for i, j in person["pets"], items():
    print(i)
