# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


'''
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

'''



#here datastore is dictionary and medical is key; the value of medical is list of dictionaris
datastore = { "medical":[
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }

      ]
}

outfile = open('retail_space.cvs', 'w')
outfile.write('room-number, use, sq.ft, price\n')

mylist = datastore['medical'] #important to understand

print(type(mylist))

#for loop
#for l in datastore['medical']:#datastore medical is list and l refers to each element on that list 
#       print(type(mylist)) #mylist is the list of dictionaries
#       outfile.write(str(1))
#       print(type(l))

for l in mylist: # l is just a iterator 
    #we have to convert string before we write to a file, whenever we import or export file we have to convert string first
    outfile.write(str(1["room-number"])+','+1["use"]+','+str(1["sq-ft"])+','+str(1["price"])+'\n')
      
outfile.close()