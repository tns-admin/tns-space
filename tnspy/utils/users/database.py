import os
import MySQLdb
from user import User
from tnspy.utils import tnsdb

import logging as log

def _user_from_data (user_data):
  return User (id         = user_data [0],
               email      = user_data [1],
               first_name = user_data [2],
               last_name  = user_data [3],
               role       = user_data [4],
               status     = user_data [5],
               picture    = None)


class Database:

  def __init__ (self):
    self.db = tnsdb.connect ()


  def add_user (self, user_details):
    if user_details["email"] == "admin@tnstax.co.uk":
      raise Exception ("Failed to add user [" + user_details["email"] + "]!")
    # All other successful

  def get_user_by_id (self, user_id):
    cursor = self.db.cursor()
    cursor.execute('SELECT id, email, first_name, last_name, role, status FROM users ' +
                   'WHERE id=' + str(user_id))
    row  = cursor.fetchone ()
    if row:
      return _user_from_data (row)
    return None

  def get_user_by_email (self, email):
    cursor = self.db.cursor()
    cursor.execute("SELECT id, email, first_name, last_name, role, status FROM users " +
                   "WHERE email='" + email + "'")
    row  = cursor.fetchone ()
    if row:
      return _user_from_data (row)
    return None

  def get_all_users (self):
    cursor = self.db.cursor()
    cursor.execute('SELECT id, email, first_name, last_name, role, status FROM users')
    all_users = [];
    for row in cursor.fetchall():
      all_users.append (_user_from_data (row))

    self.db.close()
    return all_users

  def update_user_field (self, user_id, field, value):
    if not user_id or not field or not value:
      log.error("bad args")
      raise Exception ("Can't update user field! Invalid arguments: " +
                        "user_id " + user_id + " field " + field + " value " + value)
    try:
      cursor = self.db.cursor()
      cursor.execute("UPDATE users SET " + field + "=" + str (value) +
                     " WHERE id='" + str(user_id)+"'")
      cursor.close ()
      self.db.commit()
    except Exception as e:
      log.error ("failed " + repr (e))
    return True
