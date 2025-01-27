import mysql.connector

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sms"
)

def view_grades():
    if not connection.is_connected():
        print("Could not connect to the database.")
        return

    cursor = connection.cursor()

    print("\nView Grades:")
    print("1. View grades by student ID")
    print("2. View grades by course ID")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    try:
        if choice == "1":
            student_id = int(input("Enter the student ID: "))
            sql_query = """
                SELECT g.grade_id, s.first_name, s.last_name, c.course_name, g.grade
                FROM grades g
                JOIN students s ON g.student_id = s.student_id
                JOIN courses c ON g.course_id = c.course_id
                WHERE g.student_id = %s
            """
            cursor.execute(sql_query, (student_id,))
            results = cursor.fetchall()

            if not results:
                print("No grades found for this student.")
            else:
                print("\nGrades for Student ID:", student_id)
                for row in results:
                    print(f"Grade ID: {row[0]}, Name: {row[1]} {row[2]}, Course: {row[3]}, Grade: {row[4]}")
        elif choice == "2":
            course_id = int(input("Enter the course ID: "))
            sql_query = """
                SELECT g.grade_id, s.first_name, s.last_name, c.course_name, g.grade
                FROM grades g
                JOIN students s ON g.student_id = s.student_id
                JOIN courses c ON g.course_id = c.course_id
                WHERE g.course_id = %s
            """
            cursor.execute(sql_query, (course_id,))
            results = cursor.fetchall()

            if not results:
                print("No grades found for this course.")
            else:
                print("\nGrades for Course ID:", course_id)
                for row in results:
                    print(f"Grade ID: {row[0]}, Name: {row[1]} {row[2]}, Course: {row[3]}, Grade: {row[4]}")
        elif choice == "3":
            print("Exiting...")
            return
        else:
            print("Invalid choice.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

if __name__ == "__main__":
    view_grades()

connection.close()