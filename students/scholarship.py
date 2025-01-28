import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sms"
)

def check_scholarship():
    if not connection.is_connected():
        print("Could not connect to the database.")
        return

    cursor = connection.cursor()

    student_id = int(input("Enter the student ID to check scholarship: "))

    sql_query = "SELECT first_name, last_name, gpa FROM students WHERE student_id = %s"
    cursor.execute(sql_query, (student_id,))
    student = cursor.fetchone()

    if not student:
        print("Student not found!")
        return

    first_name, last_name, gpa = student

    scholarship_percentage = 0
    if gpa >= 4.0:
        scholarship_percentage = 50
    elif gpa >= 3.5:
        scholarship_percentage = 40
    elif gpa >= 3.0:
        scholarship_percentage = 30
    elif gpa >= 2.5:
        scholarship_percentage = 20

    print(f"\nStudent: {first_name} {last_name}")
    print(f"GPA: {gpa:.2f}")
    if scholarship_percentage > 0:
        print(f"Scholarship Percentage: {scholarship_percentage}%")
    else:
        print("No scholarship available for this GPA.")

    cursor.close()

if __name__ == "__main__":
    check_scholarship()

connection.close()