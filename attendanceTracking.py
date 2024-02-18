import csv



        
class AttendanceTracker:             
    def __init__(self, student_file):
        self.students = {}
        self.student_file = student_file

    def load_students(self):
        with open(self.student_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                sClass = row['Class']
                contactInfo = row['ContactInfo']
                roll_number = row['RollNumber']
                self.students[roll_number] = Student(name, sClass, contactInfo)

    def add_student(self, name, roll_number):
        if roll_number not in self.students:
            self.students[roll_number] = Student(name, roll_number)
        else:
            print("Student with this roll number already exists.")

    def take_attendance(self, date, roll_numbers_present):
        for roll_number in roll_numbers_present:
            if roll_number in self.students:
                self.students[roll_number].mark_attendance(date, "Present")
            else:
                print(f"Student with roll number {roll_number} does not exist.")

    def view_student_attendance(self, roll_number):
        if roll_number in self.students:
            return self.students[roll_number].view_attendance()
        else:
            print("Student not found.")

    def view_class_attendance(self):
        class_attendance = {}
        for roll_number, student in self.students.items():
            class_attendance[roll_number] = student.view_attendance()
        return class_attendance

    def generate_attendance_report(self, start_date, end_date):
        attendance_report = {}
        for roll_number, student in self.students.items():
            student_attendance = {}
            for date, status in student.view_attendance().items():
                if start_date <= date <= end_date:
                    student_attendance[date] = status
            if student_attendance:
                attendance_report[student.name] = student_attendance
        return attendance_report
    
student_file = 'students_details.csv'
attendance_tracker = AttendanceTracker(student_file)
attendance_tracker.load_students()