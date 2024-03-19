# Steven Lin
# 101240382
# COMP3005-B - Assignment 3 - Q1

import psycopg2

# parameters for database connection - CHANGE AS NEEDED
dbname = 'A3-Q1'
user = 'postgres'
password = '!postgres'
host = 'localhost'
port = '5432'

# 1 - getAllStudents(): Retrieves and displays all records from the students table.
def getAllStudents():
    cursor = conn.cursor()
    try:
        query = 'SELECT * FROM students'
        cursor.execute(query)
        studentRows = cursor.fetchall()
        for student in studentRows:
            print(student)
    except psycopg2.DatabaseError as e:
        print("Error getting student records in getAllStudents()")
        conn.rollback
    finally:
        cursor.close()

# 2 - addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    cursor = conn.cursor()
    try:
        query = f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')"
        cursor.execute(query)
        conn.commit()
        print("Added new student")
    except psycopg2.DatabaseError as e:
        print("Error adding student in addStudent()")
        conn.rollback
    finally:
        cursor.close()

# 3 - updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email):
    cursor = conn.cursor()
    try:
        query = f"UPDATE students SET email = '{new_email}' WHERE student_id = '{student_id}'"
        cursor.execute(query)
        conn.commit()
        print("Updated student email")
    except psycopg2.DatabaseError as e:
        print("Error updating student's email in updateStudentEmail()")
        conn.rollback
    finally:
        cursor.close()

# 4 - deleteStudent(student_id): Deletes the record of the student with the specified student_id.
def deleteStudent(student_id):
    cursor = conn.cursor()
    try:
        query = f"DELETE FROM students WHERE student_id = '{student_id}'"
        cursor.execute(query)
        conn.commit()
        print("Deleted student records")
    except:
        print("Error deleting student records in updateStudentEmail()")
        conn.rollback
    finally:
        cursor.close()

# Establishes a connection to the database
def connectServer():
    try:
        with psycopg2.connect(
            dbname = dbname,
            user = user,
            password = password,
            host = host,
        ) as conn:
            print("Connected to the PostgreSQL server")
            return conn

    except (psycopg2.DatabaseError, Exception) as error:
            print(error)

conn = connectServer()


# Manual Testing
# getAllStudents()

# addStudent("Bob", "Smith", "bobsmith@gmail.com", "2020-01-01")
# getAllStudents()

# updateStudentEmail(1, "john.doe.NEW@gmail.com")
    
# deleteStudent(3)


conn.close()