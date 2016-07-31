mport MySQLdb


class Database:

  def __init__ (self):
    #host='173.194.236.9'
    self._db = MySQLdb.connect(unix_socket='/cloudsql/tns-space:sql-srv1',
                               port=3306,
                               db='tns_space',
                               user='space',
                               passwd='adVen4e!')

  def execute (self, statement):
    cursor = self._db.cursor ()
    cursor.execute (statement)
    rows = cursor.fetchall ()
    cursor.close ()
    return rows

