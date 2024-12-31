from attendance_system import AttendanceSystem

def main():
    system = AttendanceSystem()

    # Register students
    system.register_student("student_1")
    system.register_student("student_2")
    system.register_student("student_3")


    # Record attendance
    system.record_attendance("student_1")
    system.record_attendance("student_2")

    # Verify attendance
    system.verify_attendance()

    # Display blockchain
    system.display_blockchain()

if __name__ == "__main__":
    main()
