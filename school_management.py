from Authentication.admin_authentication import AdminAuthentication
from Authentication.teacher_authentication import TeacherAuthentication

# import Authentication.admin_authentication as admin_auth
# import Authentication.teacher_authentication as teacher_auth

print("Welcome to xoxo school manager")
print("Enter the appropriate command to perform the corresponding operation")
print("1 - Login as administrator\n2 - Log in as teacher\nq - Quit")

while True:
    command = input("Enter your preferred command or 'q' to quit: ")
    if command == "1":
        # code for administrator login
        AdminAuthentication()
    elif command == "2":
        # code for teacher login
        TeacherAuthentication()
    elif command.lower() == 'q':
        print("Exiting...")
        break
    else:
        print("Invalid command. Please enter 1, 2 or 'q to quit'.")