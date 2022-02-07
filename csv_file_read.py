import csv  # import the csv file

customers = open(
    "customers.csv", "r"
)  # this create the file object for customer in read mode

customer_file = csv.reader(
    customers, delimiter=","
)  # we read it and it create the csv object
# reader is the method of the csv module for the object csv,
# we supply the file object and tell how it delimited by comma seperator


# to skip a line if the file contains a header record
next(customer_file)

for record in customer_file:  # the object record is gonna to be a list or tuple
    print(record)
    print(type(record))  # type tells us what kind of object we are dealing with
    """
    print('first name:',record[1])
    print('last name:',record[2])
    print('City:',record[3])
    print('Country:',record[4])
    print('Phone:',record[5])
    """
    input()  # input is break, unless you type something, it shows one record at a time
