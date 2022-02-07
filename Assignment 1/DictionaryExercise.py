#create a dictionary containing course numbers and the room numbers of the rooms where courses meet.

course_and_roomnumbers = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411' }

#create a dictionary containing course numbers and names of the instructors that teach each courses.

course_and_instructor = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee' }

#create a dictionary containing course numbers and meeting times of each courses.

course_and_meetingtimes = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.' }

# keepgoing variable is to control loop
keepgoing = 'y'
while keepgoing=='y' or keepgoing == 'Y':
    #ask user to enter the course number
    courseNumber = input("Please enter the Course Number: ")
    #use if function
    if courseNumber in course_and_roomnumbers:
        #display the room number, instructor, and meeting times
        print(f"Room number is {course_and_roomnumbers[courseNumber]}, instructor's name is {course_and_instructor[courseNumber]}, and meeting time is {course_and_meetingtimes[courseNumber]}. ")
        
    else:
        print('Please enter the valid course number.')
        
    keepgoing = input("Do you want to search more course number? Please enter 'Y' or 'y' for YES and any other key for No.")

