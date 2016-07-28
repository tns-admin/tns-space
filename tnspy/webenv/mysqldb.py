import os
import MySQLdb
import logging as log

def connect ():
  log.info (os.getenv('SERVER_SOFTWARE', ''))
  return MySQLdb.connect(#host='127.0.0.1',
                         unix_socket='/cloudsql/tns-space:sql-srv1',
                         #host='173.194.236.9',
                         port=3306,
                         db='tns_space',
                         user='space',
                         charset='utf8',
                         passwd='adVen4e!')
