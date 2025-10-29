# ------------------------------------------------------------
# Program: Student Record Manager 
# Author: Aviram Dhagat
# Description:
#   This program manages student records using classes and a
#   menu-driven interface. It allows users to:
#     - Create a student list
#     - Add student data
#     - Display all records
#     - Search by roll number
#     - Identify failed students
# ------------------------------------------------------------

# ------------------------------------------------------------
# Class: Student
#   Represents a student with roll number, name, course, and marks.
# ------------------------------------------------------------
class Student:
    def __init__(self, rollno, name, course, marks):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.marks = marks  # Dictionary of subject → marks

    def __str__(self):
        return f'Student details: \n' \
               f'  Roll No: {self.rollno} \n' \
               f'  Name: {self.name} \n' \
               f'  Course: {self.course} \n' \
               f'  Marks: {self.marks}'

# ------------------------------------------------------------
# Class: data
#   Manages a list of Student objects and provides operations.
# ------------------------------------------------------------
class data:
    def __init__(self):
        self.lst = []  # List to store Student objects

    # Add a new student to the list
    def add_data(self):
        rollno = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        marks = {}
        for i in range(1, 6):
            marks[i] = int(input(f"Enter marks for subject {i}: "))
        self.lst.append(Student(rollno, name, course, marks))

    # Display all student records
    def display_all(self):
        for stud in self.lst:
            print(stud)

    # Search and display student by roll number
    def Stud_id(self):
        inputrollno = int(input("Enter the roll no: "))
        for i in self.lst:
            if i.rollno == inputrollno:
                print(i)
                return
        print("No student found with this rollno")

    # Display students who failed in any subject (marks < 40)
    def Failed_stu(self):
        for i in self.lst:
            for sub, marks in i.marks.items():
                if marks < 40:
                    print(i)
                    break

# ------------------------------------------------------------
# Menu-driven interface for interacting with the system
# ------------------------------------------------------------
while True:
    print('Press 1 for creating list \n'
          'Press 2 for adding student data \n'
          'Press 3 for displaying student data \n'
          'Press 4 for displaying data by ID \n'
          'Press 5 for displaying failed students \n'
          'Press 6 to exit \n')
    menu_num = int(input('Enter the menu num:'))

    match menu_num:
        case 1:
            s1 = data()
            print('List created successfully!')
        case 2:
            s1.add_data()
            print('Student added successfully to the list!')
        case 3:
            s1.display_all()
        case 4:
            s1.Stud_id()
        case 5:
            s1.Failed_stu()
        case 6:
            print('Exited!')
            break
        case _:
            print('Invalid input!')
