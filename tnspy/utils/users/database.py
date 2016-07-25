from user import User

import logging as log

TNS_USERS = [
  {"id": 1, "first_name": "Admin", "last_name": "Super", "email": "admin@tnstax.co.uk", "role": 1, "status": 1, "picture": None},
  {"id": 2, "first_name": "Sergii", "last_name": "Romanov", "email": "sergii.romanov@tnstax.co.uk", "role": 2, "status": 1, "picture": None},
  {"id": 3, "first_name": "Tatiana", "last_name": "Gutu", "email": "tatiana.gutu@tnstax.co.uk", "role": 2, "status": 1, "picture": None},
  {"id": 4, "first_name": "Svetlana", "last_name": "Onofrei", "email": "svetlana.onofrei@tnstax.co.uk", "role": 2, "status": 1, "picture": None},
]


def _user_from_data (user_data):
  return User (id         = user_data ["id"],
               email      = user_data ["email"],
               first_name = user_data ["first_name"],
               last_name  = user_data ["last_name"],
               role       = user_data ["role"],
               status     = user_data ["status"],
               picture    = user_data ["picture"])

class Database:

  def __init__ (self):
    self.init = True

  def add_user (self, user_details):
    if user_details["email"] == "admin@tnstax.co.uk":
      raise Exception ("Failed to add user [" + user_details["email"] + "]!")
    # All other successful

  def get_user_by_id (self, user_id):
    for user in TNS_USERS:
      if user ["id"] == user_id:
        return _user_from_data (user)
    return None

  def get_user_by_email (self, email):
    for user in TNS_USERS:
      if user ["email"] == email:
        return _user_from_data (user)
    return None

  def get_all_users (self):
    result = []
    for user in TNS_USERS:
      result.append (_user_from_data (user))
    return result

  def update_user_field (self, user_id, field, value):
    if not user_id or not field or not value:
      raise Exception ("Can't update user field! Invalid arguments: " +
                        "user_id " + user_id + " field " + field + " value " + value)
    return True
