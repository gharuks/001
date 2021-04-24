import psycopg2
from config import config

def create_tables():
    """ create tables in the PostgreSQL database"""
    command = ("""CREATE TABLE class_A(
            student_num INTEGER,
            student_name VARCHAR(255),
            student_gpa NUMERIC
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
# conn = psycopg2.connect(
#     host="localhost",
#     database="demo",
#     user="pp2user",
#     password="...")
# # create a cursor
# cur = conn.cursor()

# cur.execute("""
# CREATE TABLE users(
#         id INTEGER,
#         name VARCHAR(225),
#         faculty VARCHAR,
#         gpa NUMERIC
# )
# """)

# # close the communication with the PostgreSQL
# cur.close()
# conn.commit()
    