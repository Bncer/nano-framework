import pymysql.cursors  


def db_connect():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',                             
                             db='easy',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    try:

        with connection.cursor() as cursor:
            sql = "SELECT * FROM marvels "
            # Execute query.
            cursor.execute(sql)
            data = cursor.fetchall()
            return data

    finally:
        connection.close()

