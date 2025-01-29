# View a student
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sms"
)

def view_students():
    if not connection.is_connected():
        print("Could not connect to the database.")
        return

    cursor = connection.cursor()

    print("\nHow would you like to view student information?")
    print("1. View all students")
    print("2. View a specific student by ID")
    print("3. View students by major")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    try:
        if choice == "1":
            cursor.execute("SELECT * FROM students")
            results = cursor.fetchall()
            if not results:
                print("No students found.")
            else:
                print("\nAll Students:")
                print("-" * 60)
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Gender: {row[3]}, Major: {row[4]}, GPA: {row[5]}")
        elif choice == "2":
            student_id = int(input("Enter the student ID: "))
            cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
            student = cursor.fetchone()
            if not student:
                print("Student not found.")
            else:
                print("\nStudent Details:")
                print("-" * 60)
                print(f"ID: {student[0]}")
                print(f"Name: {student[1]} {student[2]}")
                print(f"Gender: {student[3]}")
                print(f"Major: {student[4]}")
                print(f"GPA: {student[5]}")
        elif choice == "3":
            major = input("Enter the major: ")
            cursor.execute("SELECT * FROM students WHERE major = %s", (major,))
            results = cursor.fetchall()
            if not results:
                print("No students found for the specified major.")
            else:
                print(f"\nStudents in {major}:")
                print("-" * 60)
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Gender: {row[3]}, GPA: {row[5]}")
        elif choice == "4":
            print("Exiting view mode.")
            return
        else:
            print("Invalid choice.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

if __name__ == "__main__":
    view_students()

connection.close()