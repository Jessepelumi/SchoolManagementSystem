import sys
sys.path.append(".")

from TeacherManagement.teacher_management import Teachers
from CourseManagement.course_management import Courses

class AdminAuthentication:
    def __init__(self, txt_file='Authentication/admin_credentials.txt'):
        self.txt_file = txt_file
        self.admins = self.load_data()

    def load_data(self):
        try:
            admins = []
            with open(self.txt_file, 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    admins.append({'Username': username, 'Password': password})
            return admins
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
        with open(self.txt_file, 'w') as file:
            for admin in self.admins:
                file.write(f"{admin['Username']},{admin['Password']}\n")

class Admin:
    def __init__(self):
        self.admin_authenticator = AdminAuthentication()

    def load_admin_data(self):
        self.admin_authenticator.load_data()

    def main(self):
        print("You are now in the admin dashboard")
        print("What do you want to do?")
        print("Enter the following commands to perform the corresponding operations")
        print("1: Manage Teachers")
        print("2: Manage Students")
        print("3: Manage Courses")
        print("4: Update credentials")

        while True:
            command = input("Enter the appropriate command or 'q' to Quit: ")
            if command == "1":
                # teacher dashboard here
                teacher_manager = Teachers()
                teacher_manager.run()
            elif command == "3":
                # course dashboard here
                course_manager = Courses()
                course_manager.run()
            elif command == "4":
                # change administrator credentials module here
                username = input("Enter username: ")
                current_password = input("Enter your current password: ")
                new_password = input("Enter your new password: ")

                if self.admin_authenticator.change_password(username, current_password, new_password):
                    print("Password successfully changed")
                else:
                    print("Failed to change password. Check username and current password.")
            elif command.lower() == "q":
                print("Exiting admin dashboard...")
                break
            else:
                print("Invalid command. Enter y for Yes, n for No, or q to Quit")

if __name__ == "__main__":
    admin = Admin()
    admin.main()