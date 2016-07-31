import MySQLdb

def connect ():
  #host='173.194.236.9'
  return MySQLdb.connect(unix_socket='/cloudsql/tns-space:sql-srv1',
                         port=3306,
                         db='tns_space',
                         user='space',
                         charset='utf8',
                         passwd='adVen4e!')
