import csv

students = []

print('Welcome to our student management system  ')
opt = input('what would you like to do today? \n 1. Add New Student \n 2. View and Update Student Information \n 3. Search for a Student \n 4. Remove a student information \n')
if opt == '1':


     sname = input('Enter students full name: \n')
     sclass = input('Enter students class: \n')
     srollNumber = input('Enter students roll number: \n')
     scontact = input('Enter students contact information: \n')

     class Student:
            def __init__(self, name, sClass, rollNumber, contactInfo):
               self.name = name.capitalize()
               self.sClass = sClass
               self.rollNumber = rollNumber
               self.contactInfo = contactInfo

     stud = Student(sname, sclass, srollNumber, scontact)
     students.append(stud)

     filename = 'students_details.csv'
     fieldnames = ['Name', 'Class', 'RollNumber', 'ContactInfo']

     with open(filename, 'a', newline='') as file:
         writer = csv.DictWriter(file, fieldnames=fieldnames)
         writer.writeheader()
         for student in students:
          writer.writerow({
              'Name': student.name,
              'Class': student.sClass,
              'RollNumber': student.rollNumber,
              'ContactInfo': student.contactInfo
        })
          print('Student details saved to', filename)

elif opt == '2':
    searchStudent = input('Enter the name of the student you are looking for: \n')
    def search_student(searchStudent):
        filename = 'students_details.csv'
        with open(filename, 'r') as file:
             reader = csv.DictReader(file)
             for row in reader:
                 if row['Name'].lower() == searchStudent.lower():
                     print('Student details:' )
                     print('Name:', row['Name'])
                     print('Class:', row['Class'])
                     print('Roll Number:', row['RollNumber'])
                     print('Contact Info:', row['ContactInfo'])
                     return 
    search_student(searchStudent)              

elif opt == '3':
    name = input('Enter the name of student you want to update \n')
    def update_student(name):
     filename = 'students_details.csv'
     updated_students = []
     with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'].lower() == name.lower():
                print('Student found. Enter updated details:')
                updated_name = input('Enter updated name: ')
                updated_class = input('Enter updated class: ')
                updated_roll_number = input('Enter updated roll number: ')
                updated_contact_info = input('Enter updated contact info: ')
                row['Name'] = updated_name
                row['Class'] = updated_class
                row['RollNumber'] = updated_roll_number
                row['ContactInfo'] = updated_contact_info
            updated_students.append(row)

     with open(filename, 'w', newline='') as file: 
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_students)
        print('Student details updated in', filename)
    update_student(name)