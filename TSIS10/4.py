import psycopg2
from config import config

def update_student(student_name, student_num):
    """ update student num based on the student name """
    sql = """ UPDATE class_A
                SET student_num = %s
                WHERE student_name = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (student_num, student_name))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    # Update student num 1
    update_student("student 3",3)

# conn = psycopg2.connect(
#     host="localhost",
#     database="demo",
#     user="pp2user",
#     password="...")
# # create a cursor
# cur = conn.cursor()

# sql ="""UPDATE users
#         SET gpa = %s
#         WHERE name = %s"""

# user_name = 'user 1'
# user_gpa = '3.9'
# cur.execute(sql, (user_gpa, user_name))
# # get the number of updated rows
# updated_rows = cur.rowcount
# print(updated_rows)

# # close the communication with the PostgreSQL
# cur.close()
# conn.commit()
    