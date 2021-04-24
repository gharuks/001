import psycopg2
from config import config

def insert_student(student_name):
    """ insert a new student into the class table """
    sql = """INSERT INTO class_A(student_name)
             VALUES(%s) RETURNING student_name;"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (student_name,))
        #cur.executemany(sql,student_list)
        # get the generated id back
        student_name = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return student_name

if __name__ == '__main__':
    # insert one student
    insert_student("student 3")
    # insert multiple vendors
    # insert_student_list([
    #     ('student 1',),
    #     ('student 2',),
    #     ('student 3',),
    # ])

# conn = psycopg2.connect(
#     host="localhost",
#     database="demo",
#     user="pp2user",
#     password="...")
# # create a cursor
# cur = conn.cursor()

# sql ="""INSERT INTO users(id, name, faculty, gpa)
#          VALUES('456', 'user 2', 'FIT', '3.0') RETURNING id, name, faculty, gpa"""
# # execute the INSERT statement
# cur.execute(sql)

# # close the communication with the PostgreSQL
# cur.close()
# conn.commit()
    