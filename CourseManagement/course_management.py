import csv
# from CourseManagement.course import Course
import course

class CourseManagement:
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_courses()

    def load_courses(self):
        self.courses = []
        with open(self.file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                course_name = course.Course(**row)
                self.courses.append(course_name)

    def save_courses(self):
        with open(self.file_path, mode="w", newline="") as file:
            fieldnames = ["course_name", "class_name", "teacher_id"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for course in self.courses:
                writer.writerow(vars(course))

    def create_course(self):
        course_name = input("Enter course name: ").strip()
        class_name = input("Enter class name: ").strip()
        teacher_id = input("Enter teacher id: ").strip()
        if course_name and class_name and teacher_id:
            course = course.Course(course_name, class_name, teacher_id)
            self.courses.append(course)
            self.save_courses()
            print("Course created successfully!")
        else:
            print("Invalid input. Course not created.")

    def view_course(self):
        if self.courses:
            for index, course_name in enumerate(self.courses, start=1):
                print(f"Course {index}:")
                print(course_name)
        else:
            print("No courses available.")

    def update_course(self, index):
        if 1 <= index <= len(self.courses):
            course = self.courses[index - 1]
            print("Current course details:")
            print(course)
            print("Enter new details (leave blank to keep current value):")
            new_course_name = input("Enter new course name: ").strip()
            new_class_name = input("Enter new class name: ").strip()
            new_teacher = input("Enter new teacher: ").strip()

            if new_course_name:
                course.course_name = new_course_name
            if new_class_name:
                course.class_name = new_class_name
            if new_teacher:
                course.teacher = new_teacher

            self.save_courses()
            print("Course updated successfully!")
        else:
            print("Invalid index")

    def delete_course(self, index):
        if 1 <= index <= len(self.courses):
            del self.courses[index - 1]
            self.save_courses()
            print("Course deleted successfully!")
        else:
            print("Invalid index. No course deleted.")
