import csv

class TeacherAuthentication:
    def __init__(self, csv_file = "teacher.csv"):
        self.csv_file = csv_file
        self.teachers = self.load_data()

    def load_data(self):
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            return []
        
    def authenticate(self, teacher_id, password):
        for teacher in self.teachers:
            if teacher['ID'] == teacher_id and teacher['Password'] == password:
                return True
        return False