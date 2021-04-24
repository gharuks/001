import psycopg2
from config import config

def delete_part(student_num):
    """ delete part by student num """
    conn = None
    rows_deleted = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM class_A WHERE student_num = %s", (student_num,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

if __name__ == '__main__':
    deleted_rows = delete_part(2)
    print('The number of deleted rows: ', deleted_rows)

# conn = psycopg2.connect(
#     host="localhost",
#     database="demo",
#     user="pp2user",
#     password="...")
# # create a cursor
# cur = conn.cursor()

# sql="DELETE FROM users WHERE name = %s"
# user_name = 'user 1'
# cur.execute(sql, (user_name,))
# print(cur.rowcount)
# # close the communication with the PostgreSQL
# cur.close()
# conn.commit()
    