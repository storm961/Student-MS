# Edit a student
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sms"
)

def edit_student():
    if not connection.is_connected():
        print("Could not connect to the database.")
        return

    cursor = connection.cursor()

    student_id = int(input("Enter the student ID you want to edit: "))

    check_query = "SELECT * FROM students WHERE student_id = %s"
    cursor.execute(check_query, (student_id,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    print("\nCurrent details:")
    print(f"Student ID: {student[0]}")
    print(f"First Name: {student[1]}")
    print(f"Last Name: {student[2]}")
    print(f"Gender: {student[3]}")
    print(f"Major: {student[4]}")
    print(f"GPA: {student[5]}")

    print("\nWhat would you like to edit?")
    print("1. First Name")
    print("2. Last Name")
    print("3. Major")
    print("4. GPA")
    print("5. Cancel")

    choice = input("Enter your choice (1-5): ")
    
    try:
        if choice == "1":
            new_first_name = input("Enter the new first name: ")
            update_query = "UPDATE students SET first_name = %s WHERE student_id = %s"
            cursor.execute(update_query, (new_first_name, student_id))
        elif choice == "2":
            new_last_name = input("Enter the new last name: ")
            update_query = "UPDATE students SET last_name = %s WHERE student_id = %s"
            cursor.execute(update_query, (new_last_name, student_id))
        elif choice == "3":
            new_major = input("Enter the new major: ")
            update_query = "UPDATE students SET major = %s WHERE student_id = %s"
            cursor.execute(update_query, (new_major, student_id))
        elif choice == "4":
            new_gpa = float(input("Enter the new GPA: "))
            update_query = "UPDATE students SET gpa = %s WHERE student_id = %s"
            cursor.execute(update_query, (new_gpa, student_id))
        elif choice == "5":
            print("No changes made.")
            return
        else:
            print("Invalid choice. No changes made.")
            return

        connection.commit()
        print("Student information updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
    finally:
        cursor.close()

if __name__ == "__main__":
    edit_student()

connection.close()