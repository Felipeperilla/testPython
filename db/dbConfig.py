import os
import pymysql

class ConnectDb():
    
    def __init__(self):        
        self.__db_user = 'root'
        self.__db_password = 'workdatabase'
        self.__db_name = 'cinema'
        self.__db_connection_name = 'groovy-plating-222519:us-central1:database'
        self.StartConnection()

    def StartConnection(self):
        if os.environ.get('GAE_ENV') == 'standard':
            unix_socket = '/cloudsql/{}'.format(self.__db_connection_name)
            self.cnx = pymysql.connect(user=self.__db_user, password=self.__db_password,
                                unix_socket=unix_socket, db=self.__db_name)
        else:
            host = '35.194.38.188'
            self.cnx = pymysql.connect(user=self.__db_user, password=self.__db_password,
                                host=host, db=self.__db_name)

        self.cursor = self.cnx.cursor()

    def Execute(self, sql_statement, insert):
        with self.cursor as cursor:
            cursor.execute(sql_statement)
            if not insert:
                result = cursor.fetchall()
        if insert:
            self.cnx.commit()
            result = "Executed"
        return result
    
    def CloseConnection(self):
        self.cursor.close()