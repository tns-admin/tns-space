from tnspy.utils import users
import tnspy.google_utils.users as google_users

def add_user_validate (request):
  email = request.get ("email")
  user_db = users.Database ()
  user = user_db.get_user_by_email (email)
  if user:
    return {"status": 1, "message": "User already exists!"}

  full_name = google_users.get_user_fullname (email)
  if full_name:
    return {"status": 0, "message": full_name}
  else:
    return {"status": 1, "message": "Invalid username!"}


def add_user (request):
  email = request.get ("email")
  user_db = users.Database ()
  user_details = google_users.get_user_details (email)
  user_details ["role"] = request.get ("role")
  try:
    user_db.add_user (user_details)
    return {"status": 0}
  except Exception as e:
    return {"status": 1, "message": repr (e)}


def update_user_field (request):
  try:
    users.Database().update_user_field (
      request.get ("user_id"),
      request.get ("field"),
      request.get ("value"))
    return {"status": 0}
  except Exception as e:
    return {"status": 1, "message": repr (e)}


def process_request (request):
  request_id = request.get ("request_id")
  reqs = request_id.split ('.')
  module = reqs[0] # must be 'users'
  func = reqs [1]
  if func == "add_user_validate":
    return add_user_validate (request)
  elif func == "add_user":
    return add_user (request)
  elif func == "update_user_field":
    return update_user_field (request)
  else:
    return {"status": 1, "message": "Invalid function"}
