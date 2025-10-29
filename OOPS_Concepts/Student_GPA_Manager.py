# ------------------------------------------------------------
# Program: Student GPA Manager 
# Author: Aviram Dhagat
# Description:
#   This program manages student records using classes and a
#   menu-driven interface. It allows users to:
#     - Add student data
#     - Display all records
#     - Search by student ID or name
#     - Calculate GPA based on weighted marks
# ------------------------------------------------------------

# ------------------------------------------------------------
# Class: student
#   Represents a student with ID, name, marks, and GPA.
#   GPA is calculated using weighted formula:
#     GPA = (1/3)*marks[0] + (1/2)*marks[1] + (1/4)*marks[2]
# ------------------------------------------------------------
class student:
    def __init__(self, studid, sname, marks):
        self.studid = studid
        self.sname = sname
        self.marks = marks
        self.gpa = self.GPA_calc()  # Automatically calculate GPA on creation

    def __str__(self):
        return f'Student details:\n' \
               f'  Stud ID: {self.studid}\n' \
               f'  Name: {self.sname}\n' \
               f'  Marks: {self.marks}\n' \
               f'  GPA: {self.gpa:.2f}'

    def GPA_calc(self):
        return (1/3)*self.marks[0] + (1/2)*self.marks[1] + (1/4)*self.marks[2]

# ------------------------------------------------------------
# Class: data
#   Manages a list of student objects and provides operations.
# ------------------------------------------------------------
class data:
    def __init__(self):
        self.lst = []  # List to store student objects

    # Add a new student to the list
    def add_data(self, studid, sname, marks):
        s = student(studid, sname, marks)
        self.lst.append(s)

    # Display all student records
    def display_stud(self):
        for i in self.lst:
            print(i)

    # Search and display student by ID
    def search_by_stud_id(self, searchid):
        for i in self.lst:
            if i.studid == searchid:
                print(i)

    # Search and display student by name
    def search_by_name(self, sname):
        for i in self.lst:
            if i.sname == sname:
                print(i)

    # Print GPA of a student by ID
    def calc_GPA(self, searchid):
        for i in self.lst:
            if i.studid == searchid:
                print(f"GPA of student {searchid}: {i.gpa:.2f}")

# ------------------------------------------------------------
# Step 1: Create data manager and add sample students
# ------------------------------------------------------------
s1 = data()
s1.add_data(1, "A", [34, 65, 98])
s1.add_data(2, "B", [43, 57, 78])
s1.add_data(3, "C", [69, 45, 88])
s1.add_data(4, "D", [22, 65, 91])

# ------------------------------------------------------------
# Step 2: Menu-driven interface for user interaction
# ------------------------------------------------------------
while True:
    print('Press 1 for displaying student data\n'
          'Press 2 for searching by ID\n'
          'Press 3 for searching by name\n'
          'Press 4 for calculating GPA of a student\n'
          'Press 5 to exit\n')

    menu_num = int(input('Enter the menu num:'))

    match menu_num:
        case 1:
            s1.display_stud()
        case 2:
            print('Searching by stud_id: 2')
            s1.search_by_stud_id(2)
        case 3:
            print('Searching by stud_name: A')
            s1.search_by_name('A')
        case 4:
            print('Printing GPA of stud_id: 2')
            s1.calc_GPA(2)
        case 5:
            print('Exited!')
            break
        case _:
            print('Invalid input!')
