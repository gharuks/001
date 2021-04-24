import psycopg2
from config import config

def get_values():
    """ query data from the table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT student_num, student_name FROM class_A ORDER BY student_num")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_values()

# conn = psycopg2.connect(
#     host="localhost",
#     database="demo",
#     user="pp2user",
#     password="...")
# # create a cursor
# cur = conn.cursor()
       
# sql ="SELECT id, name FROM users ORDER BY id"

# cur.execute(sql)
# rows = cur.fetchall()
# print("The number of parts: ", cur.rowcount)
# for row in rows:
#     print(row)

# # close the communication with the PostgreSQL
# cur.close()
# conn.commit()