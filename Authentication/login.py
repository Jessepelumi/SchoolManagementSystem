from admin import Admin

print("Welcome to JEOLAD School Manager")
print("Enter the appropriate command to perform the listed operations")
print("1 - Login as administrator\n2 - Log in as teacher\nq - Quit")

while True:
    command = input("Enter your preferred command or 'q' to quit: ")
    if command == "1":

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        admin = Admin()
        admin.load_admin_data()
        if admin.admin_authenticator.authenticate(username, password):
            print("Login successful. Redirecting to admin dashboard...")
            admin.main()
        else:
            print("Login failed. Wrong username or password.")
    elif command == "2":
        # code for teacher login
        pass
    elif command.lower() == 'q':
        print("Exiting School Manager...")
        break
    else:
        print("Invalid command. Please enter 1, 2 or 'q to quit'.")
