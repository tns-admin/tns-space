
GOOGLE_USERS = {
  "admin@tnstax.co.uk": {"email":"admin@tnstax.co.uk", "first_name": "Admin", "last_name": "Super"},
  "sergii.romanov@tnstax.co.uk": {"email":"sergii.romanov@tnstax.co.uk", "first_name": "Sergii", "last_name": "Romanov"},
  "tatiana.gutu@tnstax.co.uk": {"email":"tatiana.gutu@tnstax.co.uk", "first_name": "Tatiana", "last_name": "Gutu"},
  "svetlana.onofrei@tnstax.co.uk": {"email":"svetlana.onofrei@tnstax.co.uk", "first_name": "Svetlana", "last_name": "Onofrei"},
}


def get_user_fullname (email):
  if email in GOOGLE_USERS:
    usr = GOOGLE_USERS [email]
    return usr ["first_name"] + " " + usr ["last_name"]
  else:
    return None

def get_user_details (email):
  if email in GOOGLE_USERS:
    return GOOGLE_USERS [email]
  else:
    raise Exception ("Failed to retrieve google user [" + email + "]!")
