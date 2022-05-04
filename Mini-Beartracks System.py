#----------------------------------------------------
# Lab 3: Assignment 1: mini-beartracks
# 
# Author: Maithili Jadhav
# Collaborators/References: Lab 4 browser outline
#----------------------------------------------------

def header():
    '''
    Prints the header of the assignment
    '''
    print("=" * 26)
    print("Welcome to Mini-BearTracks")
    print("=" * 26)    


def menu():
    '''
    Ask's user what option they want to choose.
    If number(1,2,3,4) not entered prompts user to try again
    '''
    print()
    print("What would you like to do?")
    options = ["1. Print timetable", "2. Enroll in course" ,"3. Drop course", "4. Quit"]
    for option in options:
        print(option)
    user = input("> ")
    while user != "1" and user != "2" and user != "3" and user != "4":
        print("Sorry, invalid entry. Please enter a choice from 1 to 4.")
        user = input("> ")
        return user
    return user

    
def students():
    '''
    Opens the "students.txt" file and converts it into a dictionary and returns it 
    '''
    filename = open('students.txt', 'r')
    student_info = {}
    for line in filename:
        line = line.strip()
        line = line.split(",")
        student_info[line[0]] = line[1:]
    return student_info    

def courses():
    '''
    Opens the "courses.txt" file and converts it into a dictionary and returns it 
    '''
    filename = open('courses.txt', 'r')
    courses_info = {}
    for line in filename:
        line = line.strip()
        line = line.split(";")
        courses_info[line[0]] = line[1:]
    return courses_info

def enrollment():
    '''
    Opens the "enrollment.txt" file and converts it into a dictionary and returns it 
    '''
    filename = open('enrollment.txt', 'r')
    enrollment_info= {}
    for line in filename:
        key,value = line.strip().split(':')
        value = value.strip()
        if value not in enrollment_info:
            enrollment_info[value] = [key]
        else:
            enrollment_info[value].append(key)
    remove = enrollment_info.popitem()  # remove last item from dictionary
    return enrollment_info

def student_added(students,enrollment,courses,student_id,course_name):
    '''
    Successfully adds student (for option 1) either new or old in the enrollment dictionary.
    As parameters it takes in the student,enrollment and courses_dictionary. 
    Also takes in user's entered student_id and wanted course. 
    '''
    num = 0
    for word in list(enrollment.values()): # When user picks course, it sees if there are spaces available in the enrollment dictionary
        for specific_word in word :
            if course_name in specific_word:
                num += 1
    courses1 = courses[course_name]  # Sees maximum number of students allowed to enroll by looking at courses dictionary 
    maximum = courses1[1]
    maximum = maximum.strip()
    if int(maximum) < num: 
        print(course_name + " is already at capacity. Please contact advisor to get on waiting list.") # max students
    elif int(maximum) >= num:
        if student_id not in enrollment.keys():
            enrollment[student_id] = [course_name]  # adding new student in enrollment dictionary
        elif student_id in enrollment.keys():
            adding = enrollment[student_id].append(course_name) # adding course name
        interger = int(maximum) - 1
        string = str(interger)
        new_num = courses[course_name] 
        new_num[1] = string # adds decrease student number into dict
        student_values = students[student_id] # getting student information
        value = courses[course_name]  
        time = value[0]  # get's the time when the course is       
        name = student_values[1]  # get's the name of the student 
        print(name.strip() + " has successfully been enrolled in " + course_name + ", on" + time)    
    

def option1(students, courses, enrollment):
    '''
    Prints Timetable. Parameters are student, courses, and enrollment dictionary. 
    Is not fully finished.
    '''
    student_id = input("Student ID: ")
    if student_id not in students.keys():
        print("Invalid student ID.  Cannot print timetable.")
    elif student_id in students.keys():
        information = students[student_id] # get's the value from the dictionary for that specific student id (which is the key)
        name = information[1]  # get's the name of the student
        faculty  = information[0] # get's the faculty   
        name = name.strip()
        name = name.upper()
        faculty = faculty.strip()
        print("Timetable for " + name + ", in the faculty of " + faculty)
        class_row = [ ] 
        for x in enrollment[student_id]:  
            course = x
            class_row.append(course)  # appends the classes the student has taken in a list         
        column_header = ["8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
        row_header = ["Mon/Wed/Fri"]                                                                                                                    
        print("        ",end ="   ")
        for col in column_header:
            print('      ',col,end=' ')
        print()
        print("  "* 6+"+------------+------------+------------+------------+------------+------------+------------+------------+------------+")
        for row in row_header:
            print(row, end = " |")
            for col in column_header:
                for course in class_row:
                    a = courses[course]
                    timing = a[0]
                    timing = timing.strip()
                    timing = timing.split()
                    date = timing[0]
                    time = timing[1]
                    if date == "MWF":
                        if time == col:
                            print(" ",course, end = "  |")
        print()                    
        print("  "* 6+"+------------+------------+------------+------------+------------+------------+------------+------------+------------+")            
        new_row_header = ["Tues/Thurs"]
        for row in new_row_header:
            print(row, end = "  |")
            for course in class_row:
                a = courses[course]
                timing = a[0]
                timing = timing.strip()
                timing = timing.split()
                date = timing[0]
                time = timing[1]
                if date == "TR":
                    print(" ",course, end = "  |") 
        print()
        print("  "* 6+"+------------+------------+------------+------------+------------+------------+------------+------------+------------+")        
        
def option2(students, courses, enrollment):
    '''
    Goes through a process if student can enroll into a class.
    Takes in student, courses and enrollment dictionary. 
    '''
    student_id = input("Student ID: ")
    if student_id not in students.keys():
        print("Invalid student ID. Cannot continue with course enrollment.")
        menu()
    elif student_id in students.keys():
        course_name = input("Course name: ")
        course_name = course_name.upper()
        if course_name not in courses.keys():
            print("Invalid course name.")
            menu()
        elif course_name in courses.keys():  
            if student_id not in enrollment.keys():  # student id not in enrollment dictionary
                student_added(students,enrollment,courses,student_id,course_name)  # calls function
            elif student_id in enrollment.keys() and course_name in enrollment[student_id]: # if student id in enrollment dictionary and course name already in their enrollment info
                value = courses[course_name]
                time = value[0]
                print("already registered for course" + time +".") # already has the course registered
            elif student_id in enrollment.keys() and course_name not in enrollment[student_id]:  # if student id in enrollment dictionary and course name NOT in their enrollment info 
                value = courses[course_name]  
                time = value[0]
                for num_courses in enrollment[student_id]:
                    value2 = courses[num_courses]  
                    time2 = value[0]
                    if time == time2:
                        print("already registered for course" + time2 +".")   # already has a differnet course registered at same time
                student_added(students,enrollment,courses,student_id,course_name)  # calls function 
            
                           
def option3(students, courses, enrollment):
    '''
    Allows student to drop the course the want
    Takes in student, courses and enrollment dictionary.
    '''
    student_id = input("Student ID: ")
    if student_id not in students.keys():
        print("Invalid student ID. Cannot continue with course enrollment.")
        menu()
    elif student_id in enrollment.keys():
        class_ =  enrollment[student_id]
        sort = class_.sort()  # Puts class in alphabetical order 
        for classes in enrollment[student_id]:  
            print("- " + classes)  # Prints the classes the student has 
        user_drop = input("> ")
        user_drop = user_drop.upper()
        student_values = students[student_id]  # Getting student information
        name = student_values[1]         
        if user_drop in enrollment[student_id]:
            user_drop = user_drop.upper()
            removing = enrollment[student_id].remove(user_drop)  # Removes the course the student wants to drop from dictionary        
            print(name + " has successfully dropped " + user_drop)
        elif user_drop not in enrollment[student_id]:  # If sudent is not registered in the course wanting to drop 
            print("Drop failed. " + name + "is not currently registered in " + user_drop)
        
def option4(students, courses, enrollment):
    '''
    Adds changes to the textfile.
    Takes in student, courses and enrollment dictionary.
    '''
    filename = open('enrollment.txt', 'w')
    for key, values in enrollment.items():
        for x in values:
            filename.write(x +':' +'\n' + key + '\n')
    print("Goodbye")
    
def main():
    header()
    quit = False
    student_info = students()
    courses_info = courses()
    enrollment_info = enrollment()    
    while not quit:
        
        user = menu()
        
        if user == "1":
            option1(student_info, courses_info, enrollment_info)
            
        if user == "2":
            option2(student_info, courses_info, enrollment_info)
            
        if user == "3":
            option3(student_info, courses_info, enrollment_info)
            
        if user == "4":
            option4(student_info, courses_info, enrollment_info)
            quit = True
main()