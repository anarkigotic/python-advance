import pymysql.cursors

HOST = "localhost"
USER = "root"
PASSWORD = "Histeria182"
DATABASE = "pythonexample"

USER_TABLE = """
    CREATE TABLE  IF NOT EXISTS `users`(
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL
    )
"""
DROP_USER =""" 
    DROP TABLE IF EXISTS `users`
    """
SHOW_TABLES = """ SHOW TABLES """


INSERT_USERS = "INSERT INTO users (username,password) VALUES('{username}','{password}')"

SELECT_USERS = "select * from users where id = {id}"

UPDATE_USER = "UPDATE users set username='{username}', password= '{password}' where id = {id}"

if __name__ == "__main__":
    try:
        connection = pymysql.connect(HOST, USER, PASSWORD, DATABASE)
        curso = connection.cursor()

        # curso.execute(DROP_USER)
        # curso.execute(USER_TABLE)

        # username = input("Ingrese el username : ")
        # password = input("Ingrese el password : ")
        # query = INSERT_USERS.format(username=username,password=password)
        # curso.execute(query)


        # curso.execute(SHOW_TABLES)
        # tables = curso.fetchall()
        # for data in tables:
        #     print(data)
        # try:
        #     connection.commit()
        # except:
        #     connection.rollback()

        # query = SELECT_USERS.format(id=5)
        # curso.execute(query)
        # users = curso.fetchall()
        # print(users[0])
        # for user in users:
        #     print(user)


        query = UPDATE_USER.format(username='JUAN JEREZ',password="123",id=3)
        try:
            print(query)
            curso.execute(query)
            connection.commit()
        except:
            connection.rollback()
       
        connection.close()
    except pymysql.Error as error:
        print(error)
