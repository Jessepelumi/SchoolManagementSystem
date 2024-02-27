import sys
sys.path.append(".")

from admin_authentication import AdminAuthentication
from TeacherManagement.teacher_management import Teachers
# import TeacherManagement.teacher_management

class Admin:
    def __init__(self):
        self.admin_authenticator = AdminAuthentication()

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