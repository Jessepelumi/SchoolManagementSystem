import csv
from TeacherManagement.teacher import Teacher
from utils import generate_teacher_id

class TeacherManagement:
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_teachers()

    def load_teachers(self):
        self.teachers = []
        self.teacher_ids = set()
        with open(self.file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                teacher = Teacher(**row)
                self.teachers.append(teacher)
                self.teacher_ids.add(teacher.teacher_id)

    def save_teachers(self):
        with open(self.file_path, mode="w", newline="") as file:
            fieldnames = ["teacher_name", "teacher_id", "course", "contract_info"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for teacher in self.teachers:
                writer.writerow(vars(teacher))

    def create_teacher(self):
        teacher_name = input("Enter teacher name: ").strip()
        # teacher_id = input("Enter teacher id: ").strip()
        course = input("Enter assigned course: ").strip()
        contract_info = input("Enter the contract details: ").strip()
        if teacher_name and course and contract_info:
            teacher_id = generate_teacher_id()
            while teacher_id in self.teacher_ids:
                teacher_id = generate_teacher_id()
            teacher = Teacher(teacher_name, teacher_id, course, contract_info)
            self.teachers.append(teacher)
            self.teacher_ids.add(teacher_id)
            self.save_teachers()
            print("Teacher info successfully created!")
        else:
            print("Invalid input. Teacher info not created.")

    def view_teacher(self):
        if self.teachers:
            for index, teacher in enumerate(self.teachers, start=1):
                print(f"Teacher {index}:")
                print(teacher)
        else:
            print("No teacher available.")

    def update_teacher(self, index):
        if 1 <= index <= len(self.teachers):
            teacher = self.teachers[index - 1]
            print("Current teacher details are:")
            print(teacher)
            print("Enter new details (leave blank to keep current value):")
            new_teacher_name = input("Enter new teacher name: ").strip()
            new_course = input("Enter new course: ").strip()
            new_contract = input("Enter new contract details: ").strip()

            if new_teacher_name:
                teacher.teacher_name = new_teacher_name
            if new_course:
                teacher.course = new_course
            if new_contract:
                teacher.contract_info = new_contract