import csv;



students = []

class Student:
    def __init__(self, name, sClass, rollNumber, contactInfo):
       self.name = name.capitalize()
       self.sClass = sClass
       self.rollNumber = rollNumber
       self.contactInfo = contactInfo



stud = Student('emmanuel', 'a', 1, '09013729581')
students.append(stud)

filename = 'students_details.csv'
fieldnames = [ 'Name' , '  Class ' , '  RollNumber' , '  ContactInfo']

with open(filename, 'wt', newline='') as file :
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for Student in students:
        writer.writerow({'Name': Student.name, 'Class': Student.sClass, 'RollNumber': Student.rollNumber, 'ContactInfo': Student.contactInfo})


print('Student Details saved to', filename) 
     
