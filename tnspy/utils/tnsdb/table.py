
from database import Database

class Table (Database):
  
  def __init__ (self, table):
    #super (Database, self).__init__()
    self._table = table

  def insert (self, data):
    if not data:
      return None

    sql = "INSERT INTO " + self._table + " "
    sql += "("
    for field in data:
      sql += field + ", "
    if sql.endswith (", "):
      sql = sql [:-2]
    sql += ") VALUES ("

    for field in data:
      sql += "'" + str(data[field]) + "'" + ", "
    if sql.endswith (", "):
      sql = sql [:-2]

    sql += ")"

    return self.execute (sql)

  def select (self, data):
    sql = "SELECT "
    if not data ["fields"]:
      sql += "* "
    else:
      for field in data ["fields"]:
        sql += field + ", "
      sql = sql [:-2]

    sql += " FROM " + self._table

    if data ["where"]:
      sql += " WHERE "
      for field, val in data ["where"].iteritems ():
        sql += field + "='" + str(val) + "'"
        sql += " AND "
      sql = sql [:-5] # remove the last ' AND '

    return self.execute (sql)

  def update (self, data):
    sql = "UPDATE " + self._table + " SET "

    for field, val in data ["fields"]:
      sql += field + "='" + str (val) + "' "

    sql += " WHERE "
    for field, val in data ["where"].iteritems ():
      sql += field + "='" + str(val) + "'"
      sql += " AND "
    sql = sql [:-5] # remove the last ' AND '

    return self.execute (sql)



