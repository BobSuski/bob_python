class ConnectionManager(object):

    def open_database_r(self,db_name):
        try:
            return open(db_name,"rb+")
        except FileNotFoundError as e:
            print(e.__str__())
            return None

    def open_database_w(self,db_name):
        return open(db_name,"wb+")

    def open_database_a(self,db_name):
        return open(db_name,"ab+")

    def close_database(self,db_connection):
        db_connection.close()