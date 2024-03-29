import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
	    # execute a statement
        cur.execute('SELECT version()')
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
if __name__ == '__main__':
    connect()
# conn = psycopg2.connect(
#     host="localhost",
#     database="demo",
#     user="pp2user",
#     password="...")
# # create a cursor
# cur = conn.cursor()
# # close the communication with the PostgreSQL
# cur.close()
# conn.commit()
    