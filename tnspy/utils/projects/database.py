import MySQLdb
from project import Project
from tnspy.utils import tnsdb

import logging as log

class Database:

  _all_fields = ' id, '\
                'code, '\
                'title, '\
                'description, '\
                'client_id, '\
                'owner_id, '\
                'creator_id, '\
                'created_timestamp, '\
                'due_date, '\
                'status '


  def __init__ (self):
    self.db = tnsdb.connect ()


  def get_project_by_id (self, project_id):
    cursor = self.db.cursor()
    cursor.execute('SELECT ' + self._all_fields +
                   'FROM projects WHERE id=' + str(project_id))
    row  = cursor.fetchone ()
    if row:
      Project (row)
    return None


  def get_all_projects (self):
    cursor = self.db.cursor()
    cursor.execute('SELECT ' + self._all_fields + ' FROM projects')
    result = [];
    for row in cursor.fetchall():
      result.append (Project (row))

    self.db.close()
    return result

