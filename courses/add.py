# Add a course
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sms"
)

def add_course():
    if not connection.is_connected():
        print("Could not connect to the database.")
        return

    cursor = connection.cursor()

    course_name = input("Enter the course name: ")

    sql_query = "INSERT INTO courses (course_name) VALUES (%s)"
    try:
        cursor.execute(sql_query, (course_name,))
        connection.commit()
        print("Course added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
    finally:
        cursor.close()

if __name__ == "__main__":
    add_course()

connection.close()