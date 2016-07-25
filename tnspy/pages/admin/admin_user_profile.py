from tnspy.utils import users

def process_request (request):
  users_db = users.Database ()
  user_id = int(request.get ("id"))
  return {'user': users_db.get_user_by_id (user_id),
          'role_map': users.USER_ROLE_MAP,
          'status_map': users.USER_STATUS_MAP}
