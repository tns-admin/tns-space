from google.appengine.api import users as gusers

def validate_current_user (request_handler):
    valid_users = ["admin@tnstax.co.uk",
                   "sergii.romanov@tnstax.co.uk",
                   "tatiana.gutu@tnstax.co.uk",
                  ]
    user = gusers.get_current_user()
    if not user or user.email () not in valid_users:
        request_handler.redirect(gusers.create_login_url(request_handler.request.uri))