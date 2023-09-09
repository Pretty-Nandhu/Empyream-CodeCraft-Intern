import datetime

class Student:
    def __init_1_(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = {}

class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully!")

    def mark_attendance(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            student.attendance[date] = True
            print(f"Attendance marked for {student.name} on {date}")
        else:
            print("Student not found!")

    def view_attendance(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Attendance for {student.name}:")
            for date, attended in student.attendance.items():
                status = "Present" if attended else "Absent"
                print(f"{date}: {status}")
        else:
            print("Student not found!")

def main():
    attendance_system = AttendanceSystem()

    while True:
        print("\nAttendance Monitoring System")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            attendance_system.add_student(student_id, name)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            attendance_system.mark_attendance(student_id)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            attendance_system.view_attendance(student_id)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()