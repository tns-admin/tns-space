from tnspy.utils import users
from tnspy.google_utils import users as google_users

def process_request (request):
  response = {
    "user": users.get_current_user (),
    "logout_url": google_users.create_logout_url ()
  }
  return response
