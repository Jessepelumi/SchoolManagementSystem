class Teacher:
    def __init__(self, teacher_name, teacher_id, course, contract_info):
        self.teacher_name = teacher_name
        self.teacher_id = teacher_id
        self.course = course
        self.contract_info = contract_info

    def __str__(self):
        return f"Name: {self.teacher_name}\nTeacher ID: {self.teacher_id}\nCourse: {self.course}\nContract Info: {self.contract_info}"