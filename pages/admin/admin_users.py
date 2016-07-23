import os
import MySQLdb

from google.appengine.api import users

import jinja2
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app

"""
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
    db = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db='guestbook', user='root', charset='utf8')
else:
    db = MySQLdb.connect(host='127.0.0.1', port=3306, db='guestbook', user='root', charset='utf8')
"""

def process_request (request):
    user = users.get_current_user ()

    db = MySQLdb.connect(host='130.211.102.81', port=3306, db='tns_space', user='space', charset='utf8', passwd='adVen4e!')
#    db = MySQLdb.connect(host='/cloudsql/tns-space:europe-west1:sql-srv', port=3306, db='tns_space', user='space', charset='utf8', passwd='adVen4e!')

    cursor = db.cursor()
    cursor.execute('SELECT id, name, email FROM users')

    all_users = [];
    for row in cursor.fetchall():
      all_users.append(dict([('id',    row[0]),
                             ('name',  row[1]),
                             ('email', row[2])]))

    db.close()

    return {'all_users': all_users}