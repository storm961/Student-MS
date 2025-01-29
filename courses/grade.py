# Add grade for the course
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sms"
)

def add_grade():
    if not connection.is_connected():
        print("Could not connect to the database.")
        return

    cursor = connection.cursor()

    student_id = int(input("Enter the student ID: "))
    course_id = int(input("Enter the course ID: "))
    grade = input("Enter the grade (A/B/C/D/F): ").upper()

    sql_query = """
        INSERT INTO grades (student_id, course_id, grade)
        VALUES (%s, %s, %s)
    """
    data = (student_id, course_id, grade)

    try:
        cursor.execute(sql_query, data)
        connection.commit()
        print("Grade added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
    finally:
        cursor.close()

if __name__ == "__main__":
    add_grade()

connection.close()
