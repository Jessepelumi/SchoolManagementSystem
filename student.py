import csv
import uuid
import random

students = []

print('Welcome to our student management system  ')
def generate_short_uuid():
   
       random_number = random.randint(0, 65535)  
       uuid_string = format(random_number, '04x')

       return uuid_string
opt = input('what would you like to do today? \n 1. Add New Student \n 2. View  Student Information \n 3. Search for a Student to update details \n 4. Remove a student information \n 5. Mark Student Attendance \n')
if opt == '1':
    

     sname = input('Enter students full name: \n')
     sclass = input('Enter students class: \n')
     srollNumber = generate_short_uuid()
     scontact = input('Enter students contact information: \n')
     sattendance = 0

     class Student:
            def __init__(self, name, sClass, rollNumber, contactInfo, attendance):
               self.name = name.capitalize()
               self.sClass = sClass
               self.rollNumber = rollNumber
               self.contactInfo = contactInfo
               self.attendance = attendance
            
            # def mark_attendance(self, date, status):
            #     self.attendance[date] = status

            # def view_attendance(self):
            #   return self.attendance
 
     stud = Student(sname, sclass, srollNumber, scontact, sattendance)
     students.append(stud)

     filename = 'students_details.csv'
     fieldnames = ['Name', 'Class', 'RollNumber', 'ContactInfo','Attendance']

     with open(filename, 'a', newline='') as file:
         writer = csv.DictWriter(file, fieldnames=fieldnames)
         writer.writeheader()
         for student in students:
          writer.writerow({
              'Name': student.name,
              'Class': student.sClass,
              'RollNumber': student.rollNumber,
              'ContactInfo': student.contactInfo,
              'Attendance' : student.attendance
        })
          print(student.name,' details has been saved to', filename,'and the rollNumber = ', student.rollNumber)

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
     fieldnames = ['Name', 'Class', 'RollNumber', 'ContactInfo']
     updated_students = []
     with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'].lower() == name.lower():
                print('Student found. Enter updated details:')
                updated_name = input('Enter updated name: ')
                updated_class = input('Enter updated class: ')
                updated_roll_number = generate_short_uuid()
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

elif opt == '4':
     name = input('eneter the name of student record you want to delete 😒😒')
     def remove_student(name):
      filename = 'students_details.csv'
      tempfile = 'temp.csv'

    
      with open(filename, 'r') as file, open(tempfile, 'w', newline='') as temp:
         reader = csv.DictReader(file)
         fieldnames = reader.fieldnames

        
         writer = csv.DictWriter(temp, fieldnames=fieldnames)
         writer.writeheader()

       
         for row in reader:
            if row['Name'].lower() != name.lower():
                writer.writerow(row)

    
      import os
      os.replace(tempfile, filename)

      print(f"The student '{name}' has been removed from the student details.")

     remove_student(name)

elif opt == '5' :
    name = input('Enter the rollnumber of student to mark attendance \n')
    def update_student(name):
     filename = 'students_details.csv'
     fieldnames = ['Name', 'Class', 'RollNumber', 'ContactInfo','Attendance']
     updated_students = []
     with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['RollNumber'].lower() == name.lower():
                times = row['Attendance']
                st = row['Name'].upper()
                print(f'{st} has attended this school {times} times')
                value = int(row['Attendance'])

                updated_att =  str(value + 1)
                print(f'{st} attendance has been increased to {updated_att}')
                row['Attendance'] = updated_att
                # row['Class'] = updated_class
                # row['RollNumber'] = updated_roll_number
                # row['ContactInfo'] = updated_contact_info
            updated_students.append(row)
     with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_students)
    update_student(name)
    print('Updated students attendance')
   
   

else:
    print('Something went wrong, check the options and try again')