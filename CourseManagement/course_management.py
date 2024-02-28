import csv
import uuid

class Course:
    def __init__(self, course_name, course_id, class_name):
        self.course_name = course_name
        self.course_id = course_id
        self.class_name = class_name
        self.teacher_id = None

    def __str__(self):
        if self.teacher_id:
            return f"Course Name: {self.course_name}\nCourse ID: {self.course_id}\nClass: {self.class_name}\nTeacher ID: {self.teacher_id}"
        else:
            return f"Course Name: {self.course_name}\nCourse ID: {self.course_id}\nClass: {self.class_name}\nTeacher ID: Not assigned"
    
    def assign_teacher(self, teacher_id):
        self.teacher_id = teacher_id

def generate_course_id():
    return str(uuid.uuid4())[:4]

class CourseManagement:
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_courses()

    def load_courses(self):
        self.courses = []
        self.course_ids = set()
        with open(self.file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                course_instance = Course(**row)
                self.courses.append(course_instance)

    def save_courses(self):
        with open(self.file_path, mode="w", newline="") as file:
            fieldnames = ["course_name", "course_id", "class_name", "teacher_id"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for course in self.courses:
                writer.writerow(vars(course))

    def create_course(self):
        course_name = input("Enter course name: ").strip()
        class_name = input("Enter class name: ").strip()
        # teacher_id = input("Enter teacher id: ").strip()
        if course_name and class_name:
            course_id = generate_course_id()
            while course_id in self.course_ids:
                course_id = generate_course_id()
            course_instance = Course(course_name, course_id, class_name)
            self.courses.append(course_instance)
            self.course_ids.add(course_id)
            self.save_courses()
            print("Course created successfully!")
        else:
            print("Invalid input. Course not created.")

    def assign_teacher_to_course(self, course_id, teacher_id):
        # Find the course with the given ID
        course = None
        for course_instance in self.courses:
            if course_instance.course_id == course_id:
                course = course_instance
                break

        if course:
            # Assign the teacher to the course
            course.assign_teacher(teacher_id)
            self.save_courses()
            print("Teacher assigned to course successfully!")
        else:
            print("Course not found.")

    def view_course(self):
        if self.courses:
            for index, course_instance in enumerate(self.courses, start=1):
                print(f"Course {index}:")
                print(course_instance)
        else:
            print("No courses available.")

    def search_course_by_id(self, course_id):
        found = False
        for course_instance in self.courses:
            if course_instance.course_id == course_id:
                print("Course found:")
                print(course_instance)
                found = True
                break

        if not found:
            print("Course not found.")

    def search_course_by_name(self, name):
        found = False
        for course_instance in self.courses:
            if course_instance.course_name.lower() == name.lower():
                print("Course found:")
                print(course_instance)
                found = True

        if not found:
            print("Course not found.")

    def update_course(self, course_id):
        found = False
        for course_instance in self.courses:
            if course_instance.course_id == course_id:
                print("Current course details: ")
                print(course_instance)
                print("Enter new details (leave blank to keep current value):")
                new_course_name = input("Enter new course name: ").strip()
                new_class_name = input("Enter new class name: ").strip()
                # new_teacher = input("Enter new teacher: ").strip()
            
                if new_course_name:
                    course_instance.course_name = new_course_name
                if new_class_name:
                    course_instance.class_name = new_class_name
                # if new_teacher:
                #     course_instance.teacher = new_teacher

                found = True
                break

        if not found:
            print("Course not found")

        self.save_courses()
        print("Course details updated successfully!")

    def delete_course(self, course_id):
        for i, course_instance in enumerate(self.courses):
            if course_instance.course_id == course_id:
                del self.courses[i]
                self.save_courses()
                print("Course details deleted successfully!")
                return
        print("Course not found.")

class Courses():
    def __init__(self):
        self.course_manager = CourseManagement(file_path = "CourseManagement/courses.csv")

    def run(self):
        print("Welcome to the Course Manager")
        print("What do you want to do?")
        print("Enter the following commands to perform the corresponding operations")
        print("Create courses -> 1")
        print("View courses -> 2")
        print("Search courses by ID -> 3")
        print("Search courses by name -> 4")
        print("Assign teacher -> 5")
        print("Update courses -> 6")
        print("Delete courses -> 7")
        print("Exit -> 'q'")

        while True:
            command = input("Enter your preferred command or 'q' to quit: ")

            if command == '1':
                self.course_manager.create_course()
            elif command == '2':
                self.course_manager.view_course()
            elif command == '3':
                course_id = input("Enter the ID of the course to search: ")
                self.course_manager.search_course_by_id(course_id)
            elif command == '4':
                course_name = input("Enter the name of the course to search: ")
                self.course_manager.search_course_by_name(course_name)
            elif command == '5':
                course_id = input("Enter the ID of the course: ")
                teacher_id = input("Enter the ID of the teacher to assign: ")
                self.course_manager.assign_teacher_to_course(course_id, teacher_id)
            elif command == '6':
                index = input("Enter the ID of the course to update: ")
                self.course_manager.update_course(index)
            elif command == '7':
                index = input("Enter the ID of the course to delete: ")
                self.course_manager.delete_course(index)
            elif command.lower() == 'q':
                print("Exiting Course Manager...")
                break
            else:
                print("Invalid command. Please enter a valid command")

if __name__ == "__main__":
    manager = Courses()
    manager.run()
