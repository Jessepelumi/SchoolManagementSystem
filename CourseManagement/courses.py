from CourseManagement.course_management import CourseManagement

def main():
    print("Welcome to the Course Manager")
    print("What do you want to do?")
    print("Enter the following commands to perform the corresponding operations")
    print("1: Create courses\n2: View courses\n3: Update courses\n4: Delete courses")

    course_manager = CourseManagement(file_path="courses.csv")

    while True:
        command = input("Enter your preferred command or 'q' to quit: ")
        if command == '1':
            course_manager.create_course()
        elif command == '2':
            course_manager.view_course()
        elif command == '3':
            index = int(input("Enter the index of the course to update: "))
            course_manager.update_course(index)
        elif command == '4':
            index = int(input("Enter the index of the course to delete: "))
            course_manager.delete_course(index)
        elif command.lower() == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid command. Please enter 1, 2, 3, 4, or 'q to quit'.")

if __name__ == "__main__":
    main()