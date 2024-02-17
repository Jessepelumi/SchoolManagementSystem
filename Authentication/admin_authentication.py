import csv

class AdminAuthentication:
    def __init__(self, csv_file='admin_credentials.csv'):
        self.csv_file = csv_file
        self.admins = self.load_data()

    def load_data(self):
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            return []

    def authenticate(self, username, password):
        for admin in self.admins:
            if admin['Username'] == username and admin['Password'] == password:
                return True
        return False
    
    def change_password(self, username, current_password, new_password):
        for admin in self.admins:
            if admin['Username'] == username and admin['Password'] == current_password:
                admin['Password'] = new_password
                self.save_data()
                return True
        return False
    
    def save_data(self):
        with open(self.csv_file, 'w', newline='') as file:
            fieldnames = ['Username', 'Password']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.admins)