class Course:
    def __init__(self, course_name, class_name, teacher_id):
        self.course_name = course_name
        self.class_name = class_name
        self.teacher_id = teacher_id

    def __str__(self):
        return f"Course Name: {self.course_name}\nClass: {self.class_name}\nTeacher ID: {self.teacher_id}"
