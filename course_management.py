import csv
from course import Course

class CourseManagement:
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_courses()

    def load_courses(self):
        self.courses = []
        with open(self.file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                course = Course(**row)
                self.courses.append(course)

    def save_courses(self):
        with open(self.file_path, mode="w", newline="") as file:
            fieldnames = ["course_name", "class_name", "course", "teacher"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for course in self.courses:
                writer.writerow(vars(course))

    def create_course(self, course_name, class_name, course, teacher):
        course = Course(course_name, class_name, course, teacher)
        self.courses.append(course)
        self.save_courses()

    def view_course(self):
        for index, course in enumerate(self.courses, start=1):
            print(f"Course {index}:")
            print(course)

    def update_course(self, index, **kwargs):
        if 1 <= index and index <= len(self.courses):
            course = self.courses[index - 1]
            course.teacher = kwargs.get("teacher", course.teacher)
            self.save_courses()
        else:
            print("Invalid index")

    def delete_course(self, index):
        if 1 <= index and index <= len(self.courses):
            del self.courses[index - 1]
            self.save_courses()
        else:
            print("Invalid index")