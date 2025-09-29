# Students Management Project

class StudentManagement:
    def __init__(self):
        self.students = {}  # Key= student_id, Value = student_name

        self.attendance = {}  # Store Key = student_id, Value = "Present" or "Absent"

    # student add method
    def add_student(self):
        # Ask user for student ID and name
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")

        if student_id in self.students:
            print("This student ID already exists.")

        else:
            self.students[student_id] = name
            print(f"Student '{name}' with ID {student_id} added successfully.")
    
    # view student method
    def view_students(self):
        # Check if there are students
        if not self.students:
            print("No students have been added yet.")
            return

        print("\n--- Student List ---")
        for student_id, name in self.students.items():
            status = self.attendance.get(student_id, "Not Marked")
            print(f"ID: {student_id}, Name: {name}, Attendance: {status}")
        print("---------------------\n")

    # Mark_attendance method
    def mark_attendance(self):
        student_id = input("Enter student ID to mark attendance: ")

        if student_id in self.students:
            status = input("Mark as (Present/Absent): ").capitalize()
            if status in ["Present", "Absent"]:
                self.attendance[student_id] = status
                print(
                    f"Attendance for {self.students[student_id]} set to {status}.")

            else:
                print("Invalid input. Please enter 'Present' or 'Absent'.")
        else:
            print("Student ID not found.")

    def menu(self):
        while True:
            print("\n----- Student Management Menu----")
            print("[1] Add Student")
            print("[2] View Students")
            print("[3] Mark Attendance")
            print("[4] Exit")

            choice = input("Please choose option: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.mark_attendance()
            elif choice == '4':
                print("Exiting.... Goodbye")
                
                break

            else: 
                print("Invalid option")

if __name__ == "__main__":
    sm = StudentManagement()
    sm.menu()