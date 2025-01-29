# Add a student
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sms"
)

def add_student():
    if not connection.is_connected():
        print("Could not connect to the database.")
        return

    cursor = connection.cursor()

    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    gender = input("Enter student's gender (Male/Female): ")
    major = input("Enter student's major: ")
    gpa = input("Enter student's GPA: ")

    sql_query = """
        INSERT INTO students (first_name, last_name, gender, major, gpa)
        VALUES (%s, %s, %s, %s, %s)
    """

    data = (first_name, last_name, gender, major, gpa)

    try:
        cursor.execute(sql_query, data)
        connection.commit()
        print("Student added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()

    cursor.close()

if __name__ == "__main__":
    add_student()

connection.close()