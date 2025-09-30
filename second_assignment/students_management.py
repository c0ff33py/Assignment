# Students Management Project(File Handling)

class StudentManagement:
    def __init__(self):
        self.students_file = "students.txt"
        self.attendance_file = "attendance.txt"

        # Load data from files
        self.students = self.load_students() # Key= student_id, value= Student name
        self.attendance = self.load_attendance() # Key=student_id, Value= Present/Absent

    # file Handling
    def load_students(self):
        students = {}
        try:
            with open(self.students_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        student_id, name = line.split(",")
                        students[student_id] = name
        except FileNotFoundError:
            pass # no file yet
        return students
    
    def save_students(self):
        with open(self.students_file, 'w', encoding="utf-8") as f:
            for student_id, name in self.students.items():
                f.write(f"{student_id}, {name}\n")

    def load_attendance(self):
        attendance = {}
        try:
            with open(self.attendance_file, 'r', encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        student_id, status = line.split(",")
                        attendance[student_id] = status
        except FileNotFoundError:
            pass
        return attendance
    
    def save_attendance(self):
        with open(self.attendance_file, 'w', encoding="utf-8") as f:
            for student_id, status in self.attendance.items():
                f.write(f"{student_id}, {status}\n")


    # Features
    def add_student(self):
        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()

        if student_id in self.students:
            print("This student ID already exists.")
        else:
            self.students[student_id] = name
            self.save_students()
            print(f"Student '{name}' with ID {student_id} add successfully.")
    
    def view_students(self):
        if not self.students:
            print("No students have been added yet.")
            return
        print('------Students List--------')
        for student_id, name in self.students.items():
            status = self.attendance.get(student_id, "Not Marked")
            print(f"ID :{student_id}, Name: {name}, Attendance: {status}")
            print("------------------------\n")

    def mark_attendance(self):
        student_id = input("Enter student ID to mark attendance: ").strip()
        
        if student_id in self.students:
            status = input("Mark as (Present/Absent:): ").capitalize()
            if status in ["Present", "Absent"]:
                self.attendance[student_id] = status
                self.save_attendance()
                print(f"Attendance for {self.students[student_id]} set to {status}.")
            else:
                print("Invalid input. Please enter 'Present' or 'Absent'.")    
        else:
            print("Student ID not found.")            
    def menu(self):
        while True:
            print("\n----- Student Management Menu ----")
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
            elif choice == "4":
                print("Exiting... Goodbye")
                break
            else:
                print("Invalid option")


if __name__ == "__main__":
    sm = StudentManagement()
    sm.menu()
            
            