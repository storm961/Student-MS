import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sms"
)

def calculate_gpa(student_id):
    if not connection.is_connected():
        print("Could not connect to the database.")
        return

    cursor = connection.cursor()

    sql_query = "SELECT grade FROM grades WHERE student_id = %s"
    cursor.execute(sql_query, (student_id,))
    grades = cursor.fetchall()

    if not grades:
        print("No grades found for this student.")
        return

    grade_to_gpa = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }

    total_gpa = sum(grade_to_gpa[grade[0]] for grade in grades)
    gpa = total_gpa / len(grades)

    update_query = "UPDATE students SET gpa = %s WHERE student_id = %s"
    try:
        cursor.execute(update_query, (gpa, student_id))
        connection.commit()
        print(f"GPA updated successfully! New GPA: {gpa:.2f}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
    finally:
        cursor.close()

if __name__ == "__main__":
    student_id = int(input("Enter the student ID to update GPA: "))
    calculate_gpa(student_id)

connection.close()