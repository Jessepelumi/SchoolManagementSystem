import csv

class TeacherManagement:
    def __init__(self, csv_file='teacher.csv'):
        self.teachers = []
        self.csv_file = csv_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                self.teachers = list(reader)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.csv_file, 'w', newline='') as file:
            fieldnames = ['ID', 'Name', 'Subject', 'Contact']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.teachers)

    def add_teacher(self):
        name = input('Enter teacher name: ')
        subject = input('Enter subject: ')
        contact = input('Enter contact information: ')

        if not name or not subject or not contact:
            print("Invalid input. Please provide all information.")
            return

        # Generate a unique ID for the new teacher
        new_teacher_id = len(self.teachers) + 1
        new_teacher = {'ID': new_teacher_id, 'Name': name, 'Subject': subject, 'Contact': contact}
        self.teachers.append(new_teacher)
        self.save_data()
        print(f'Teacher {name} added successfully with ID: {new_teacher_id}.')

    def view_teachers(self):
        if not self.teachers:
            print("No teachers available.")
            return

        for teacher in self.teachers:
            print(f"ID: {teacher.get('ID', 'N/A')}, Name: {teacher.get('Name', 'N/A')}, Subject: {teacher.get('Subject', 'N/A')}, Contact: {teacher.get('Contact', 'N/A')}")

    def search_teacher(self):
        keyword = input('Enter name, subject, or ID to search: ')
        found_teachers = [teacher for teacher in self.teachers if str(keyword).lower() in (str(teacher['ID']).lower(), teacher['Name'].lower(), teacher['Subject'].lower())]

        if not found_teachers:
            print(f'No teachers found with ID, Name, or Subject containing "{keyword}".')
        else:
            print("Found teachers:")
            for teacher in found_teachers:
                print(f"ID: {teacher['ID']}, Name: {teacher['Name']}, Subject: {teacher['Subject']}, Contact: {teacher['Contact']}")

    def update_teacher(self):
        teacher_id = input('Enter teacher ID to update: ')
        found_teacher = next((teacher for teacher in self.teachers if str(teacher['ID']) == str(teacher_id)), None)

        if found_teacher is None:
            print(f'Teacher with ID "{teacher_id}" not found.')
            return

        new_name = input('Enter new name (press Enter to keep the current name): ')
        new_subject = input('Enter new subject (press Enter to keep the current subject): ')
        new_contact = input('Enter new contact information (press Enter to keep the current contact): ')

        if new_name:
            found_teacher['Name'] = new_name
        if new_subject:
            found_teacher['Subject'] = new_subject
        if new_contact:
            found_teacher['Contact'] = new_contact

        self.save_data()
        print(f'Teacher with ID "{teacher_id}" updated successfully.')

    def remove_teacher(self):
        teacher_id = input('Enter teacher ID to remove: ')
        self.teachers = [teacher for teacher in self.teachers if str(teacher['ID']) != str(teacher_id)]
        self.save_data()
        print(f'Teacher with ID "{teacher_id}" removed successfully.')

# Interactive command-line interface
teacher_manager = TeacherManagement()

while True:
    print("\nJeolad International College. This is the Teacher Management Section.\n Enter any command to start:")
    print("1. Add Teacher (add)")
    print("2. View Teachers (view)")
    print("3. Search Teacher (search)")
    print("4. Update Teacher (update)")
    print("5. Remove Teacher (remove)")
    print("6. Exit (exit)")

    command = input("Enter command: ")

    if command.lower() == 'add':
        teacher_manager.add_teacher()
    elif command.lower() == 'view':
        teacher_manager.view_teachers()
    elif command.lower() == 'search':
        teacher_manager.search_teacher()
    elif command.lower() == 'update':
        teacher_manager.update_teacher()
    elif command.lower() == 'remove':
        teacher_manager.remove_teacher()
    elif command.lower() == 'exit':
        print("Exiting Teacher Management Section. Goodbye!")
        break
    else:
        print("Invalid command. Please enter a valid command.")
