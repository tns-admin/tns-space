import MySQLdb

from tnspy.utils import tnsdb
from client import Client


class Database (tnsdb.Table):

  def __init__ (self, table):
    super (tnsdb.Table, self).__init__("clients")

  def add_client (self, data):
    return self.insert (data)

  def get_client (self, client_id):
    rows = self.select ({"fields": None,
                         "where": {
                            "id": client_id
                          }
                        })
    if rows:
      return Client (rows [0])
    else:
      return None

  def get_all_clients (self, client_id):
    rows = self.select ({"fields": None,
                         "where": None
                        })
    result = []
    for row in rows:
      return result.append (Client (row))

    return result

  def update_client (self, client_id, data):
    self.update ({ "fields": data,
                   "where": {
                      "id": client_id
                    }
                 })


