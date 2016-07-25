from tnspy.google_utils import users as google_users
from database import Database as users_db

def get_current_user ():
  email = google_users.get_current_user_email ()
  return users_db().get_user_by_email (email)
