import sys
sys.path.append(".")

from admin_authentication import AdminAuthentication
from TeacherManagement.teacher import TeacherManagement

admin_authenticator = AdminAuthentication()

print("You are now in the admin dashboard")
print("Do you want to work on the teacher dashboard")

while True:
    command = input("y for Yes; n for No; q to Quit: ")
    if command.lower() == "y":
        # teacher dashboard here
        TeacherManagement()
    elif command.lower() == "n":
        print("Will you like to change administrator's credentials?")
        sub_command = input("y for Yes; n for No: ")
        if sub_command.lower() == "y":
            # change administrator credentials module here
            username = input("Enter username: ")
            current_password = input("Enter your current password: ")
            new_password = input("Enter your new password: ")

            if admin_authenticator.change_password(username, current_password, new_password):
                print("Passwword sucessfully changed")
            else:
                print("Failed to change password. Check username and current password.")

        elif sub_command.lower() == "n":
            print("Exiting...")
            break
        else:
            print("Invalid command. Enter y for Yes or n for No")
    elif command.lower() == "q":
        print("Exiting admin dashboard...")
        break
    else:
        print("Invalid command. Enter y for Yes, n for No or q to Quit")