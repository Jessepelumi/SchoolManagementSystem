import csv
import uuid

class Teacher:
    def __init__(self, teacher_name, teacher_id, course, contract_info):
        self.teacher_name = teacher_name
        self.teacher_id = teacher_id
        self.course = course
        self.contract_info = contract_info

    def __str__(self):
        return f"Name: {self.teacher_name}\nTeacher ID: {self.teacher_id}\nCourse: {self.course}\nContract Info: {self.contract_info}"

def generate_teacher_id():
    return str(uuid.uuid4())[:8]

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
                teacher_instance = Teacher(**row)
                self.teachers.append(teacher_instance)
                self.teacher_ids.add(teacher_instance.teacher_id)

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
            teacher_instance = Teacher(teacher_name, teacher_id, course, contract_info)
            self.teachers.append(teacher_instance)
            self.teacher_ids.add(teacher_id)
            self.save_teachers()
            print("Teacher info successfully created!")
        else:
            print("Invalid input. Teacher info not created.")

    def view_teachers(self):
        if self.teachers:
            for index, teacher in enumerate(self.teachers, start=1):
                print(f"Teacher {index}:")
                print(teacher)
        else:
            print("No teacher available.")

    def search_teacher_by_id(self, teacher_id):
        found = False
        for teacher_instance in self.teachers:
            if teacher_instance.teacher_id == teacher_id:
                print("Teacher found:")
                print(teacher_instance)
                found = True
                break

        if not found:
            print("Teacher not found.")

    def search_teacher_by_name(self, name):
        found = False
        for teacher_instance in self.teachers:
            if teacher_instance.teacher_name.lower() == name.lower():
                print("Teacher found:")
                print(teacher_instance)
                found = True

        if not found:
            print("Teacher not found.")

    def update_teacher(self, teacher_id):
        found = False
        for teacher_instance in self.teachers:
            if teacher_instance.teacher_id == teacher_id:
                print("Current teacher details:")
                print(teacher_instance)
                print("Enter new details (leave blank to keep current value):")
                new_teacher_name = input("Enter new teacher name: ").strip()
                new_course = input("Enter new course: ").strip()
                new_contract = input("Enter new contract details: ").strip()

                if new_teacher_name:
                    teacher_instance.teacher_name = new_teacher_name
                if new_course:
                    teacher_instance.course = new_course
                if new_contract:
                    teacher_instance.contract_info = new_contract

                found = True
                break

        if not found:
            print("Teacher not found.")

        self.save_teachers()
        print("Teacher info updated successfully!")

    def delete_teacher(self, teacher_id):
        for i, teacher_instance in enumerate(self.teachers):
            if teacher_instance.teacher_id == teacher_id:
                del self.teachers[i]
                self.save_teachers()
                print("Teacher info deleted successfully!")
                return
        print("Teacher not found.")

class Teachers:
    def __init__(self):
        self.teacher_manager = TeacherManagement(file_path="TeacherManagement/teacher.csv")

    def run(self):
        print("Welcome to the Teacher Manager")
        print("Enter the appropriate command to start: ")
        print("1. Add Teacher -> add")
        print("2. View Teachers -> view")
        print("3. Search Teacher by ID -> searchid")
        print("3. Search Teacher by name -> searchnm")
        print("4. Update Teacher -> update")
        print("5. Delete Teacher -> delete")
        print("6. Exit -> exit")

        while True:
            command = input("Enter command: ")

            if command.lower() == 'add':
                self.teacher_manager.create_teacher()
            elif command.lower() == 'view':
                self.teacher_manager.view_teachers()
            elif command.lower() == 'searchid':
                teacher_id = input("Enter the ID of the teacher to search: ")
                self.teacher_manager.search_teacher_by_id(teacher_id)
            elif command.lower() == 'searchnm':
                teacher_name = input("Enter the name of the teacher to search: ")
                self.teacher_manager.search_teacher_by_name(teacher_name)
            elif command.lower() == 'update':
                teacher_id = input("Enter the ID of the teacher to update: ")
                self.teacher_manager.update_teacher(teacher_id)
            elif command.lower() == 'delete':
                teacher_id = input("Enter the ID of the teacher to delete: ")
                self.teacher_manager.delete_teacher(teacher_id)
            elif command.lower() == 'exit':
                print("Exiting Teacher Manager...")
                break
            else:
                print("Invalid command. Please enter a valid command.")

if __name__ == "__main__":
    manager = Teachers()
    manager.run()