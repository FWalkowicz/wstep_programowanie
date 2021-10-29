import mysql.connector
from mysql.connector import Error

try:
    database_connection = mysql.connector.connect(host='localhost',
                                                  database='passwd_manager_db',
                                                  user='root',
                                                  password='')
    if database_connection.is_connected():
        print('server info: ', database_connection.get_server_info())
        cursor = database_connection.cursor()
        cursor.execute("select database();")
        print("connected db: ", cursor.fetchone())

except Error as e:
    print("there was some error with connecting", e)


def login_db(login, passwd):
    mycursor = database_connection.cursor()
    query = "SELECT unique_key FROM login WHERE login = %s and password=%s"
    data = (login, passwd)
    mycursor.execute(query, data)
    result = mycursor.fetchall()

    for i in result:
        print(result)




