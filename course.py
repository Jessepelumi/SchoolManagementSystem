class Course:
    def __init__(self, course_name, class_name, course, teacher):
        self.course_name = course_name
        self.class_name = class_name
        self.course = course
        self.teacher = teacher

    def __str__(self):
        return f"Subject Name: {self.course_name}\nClass: {self.class_name}\nCourse: {self.course}\nTeacher: {self.teacher}"
    
