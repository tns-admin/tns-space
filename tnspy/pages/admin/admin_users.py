from tnspy.utils import users

def process_request (request):
  users_db = users.Database ()

  all_users = []
  for user in users_db.get_all_users ():
    all_users.append ({
        "id": user.id (),
        "name": user.full_name (),
        "email": user.email (),
        "role": users.role_to_str(user.role ()),
        "status": users.status_to_str(user.status ())
      })
  return {'all_users': all_users}
